import json
import logging
from types import SimpleNamespace
from typing import Optional

from django.conf import settings
from openai import OpenAI

from .dataclasses import AiMovie
from .errors import AiResponseError
from .system_prompts import find_movie_system_prompt, recommendations_system_prompt, top_movies_system_prompt

logger = logging.getLogger(__name__)

STREAM_RESPONSE_FORMAT_INSTRUCTION = """
STREAMING RESPONSE FORMAT:
- Keep all language, relevance, and title-selection rules above. This section changes ONLY the response format.
- Return newline-delimited JSON only (NDJSON / JSON Lines).
- Each line must be one JSON object: {"title": "English IMDb title", "year": "YYYY", "match_score": 0-100}
- Emit one complete title object per line as soon as it is ready.
- Do not wrap the response in a JSON array.
- Do not use Markdown, numbering, comments, or extra prose.
"""


def _count_tokens_openai(text: str, model: str) -> int:
    """Count tokens for OpenAI models using tiktoken."""
    try:
        import tiktoken

        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except Exception:
        return len(text) // 4


class FindMovieAiClient:
    DEFAULT_MODEL = 'gpt-5-mini'
    DEFAULT_MAX_TOKENS = 2048
    MAX_EMPTY_LENGTH_RETRIES = 1
    SYSTEM_PROMPT: str | None = None

    def __init__(
        self,
        *,
        system_prompt: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> None:
        resolved_prompt = system_prompt or self.SYSTEM_PROMPT
        self.system_prompt = resolved_prompt
        self.model = model or self.DEFAULT_MODEL
        self.max_tokens = max_tokens or self.DEFAULT_MAX_TOKENS
        self._client: Optional[OpenAI] = None

    def find_movies(self, user_prompt: str) -> list[AiMovie]:
        if self.count_tokens(user_prompt) > settings.MAX_PROMPT_TOKENS_LENGTH:
            return []

        result: list[AiMovie] = []
        for attempt in range(self.MAX_EMPTY_LENGTH_RETRIES):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    max_completion_tokens=self.max_tokens,
                    messages=[
                        {'role': 'system', 'content': self.system_prompt or ''},
                        {'role': 'user', 'content': user_prompt},
                    ],
                )
            except Exception as exc:
                logger.exception('AI request failed: %s', exc)
                raise Exception(f'Error while finding movies: {exc}') from exc
            raw_text = response.choices[0].message.content if response.choices else ''
            finish_reason = response.choices[0].finish_reason if response.choices else 'no_choices'
            logger.info(
                'AI response: model=%s finish_reason=%s raw_prefix=%r',
                self.model,
                finish_reason,
                raw_text[:500] if raw_text else '',
            )
            wrapped = SimpleNamespace(content=[SimpleNamespace(text=raw_text or '[]')])
            result = self._parse_response(wrapped)
            should_retry_empty_length = not result and finish_reason == 'length' and attempt < self.MAX_EMPTY_LENGTH_RETRIES - 1
            if not should_retry_empty_length:
                return result
            logger.warning('AI returned empty response with finish_reason=length, retrying')

        return result

    def stream_movies(self, user_prompt: str):
        if self.count_tokens(user_prompt) > settings.MAX_PROMPT_TOKENS_LENGTH:
            return

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                max_completion_tokens=self.max_tokens,
                stream=True,
                messages=[
                    {'role': 'system', 'content': self._stream_system_prompt()},
                    {'role': 'user', 'content': user_prompt},
                ],
            )
        except Exception as exc:
            logger.exception('AI streaming request failed: %s', exc)
            raise Exception(f'Error while streaming movies: {exc}') from exc

        buffer = ''
        for chunk in stream:
            content = self._extract_stream_content(chunk)
            if not content:
                continue

            buffer += content
            lines = buffer.split('\n')
            buffer = lines.pop() or ''

            for line in lines:
                movie = self._parse_stream_line(line)
                if movie:
                    yield movie

        if buffer.strip():
            movie = self._parse_stream_line(buffer)
            if movie:
                yield movie

    def _stream_system_prompt(self) -> str:
        prompt = self.system_prompt or ''
        prompt = prompt.replace(
            'Return a JSON array of real titles that match.',
            'Return real titles that match. Use the streaming response format below.',
        )
        prompt = prompt.replace(
            'Pure JSON array: [{"title": "Exact IMDb Title", "year": "1999", "match_score": 90}, ...].',
            'NDJSON: one JSON object per line, e.g. {"title": "Exact IMDb Title", "year": "1999", "match_score": 90}.',
        )
        prompt = prompt.replace('Respond only with the JSON array.', 'Respond only with NDJSON lines.')
        return f'{prompt}\n\n{STREAM_RESPONSE_FORMAT_INSTRUCTION}'

    def count_tokens(self, user_prompt: str) -> int:
        full_text = (self.system_prompt or '') + '\n' + user_prompt
        return _count_tokens_openai(full_text, self.model)

    @staticmethod
    def _extract_stream_content(chunk) -> str:
        choices = getattr(chunk, 'choices', None) or []
        if not choices:
            return ''
        delta = getattr(choices[0], 'delta', None)
        return getattr(delta, 'content', None) or ''

    @staticmethod
    def _parse_stream_line(line: str) -> AiMovie | None:
        text = line.strip()
        if not text:
            return None

        try:
            raw = json.loads(text)
        except Exception as exc:
            logger.warning('AI stream parse failed: exc=%s raw_line=%r', exc, text[:500])
            raise AiResponseError(f'Failed to parse AI stream line: {exc}') from exc

        if isinstance(raw, dict):
            movie = AiMovie.from_dict(raw)
        elif isinstance(raw, str):
            movie = AiMovie(title=raw, match_score=0)
        else:
            raise AiResponseError(f'AI stream returned invalid item type, expected dict or str, got {type(raw)}')

        if not movie.title.strip():
            return None
        return movie

    @staticmethod
    def _parse_response(response) -> list[AiMovie]:
        try:
            raw = json.loads(response.content[0].text)

            if not isinstance(raw, list):
                raise AiResponseError(f'AI returned invalid format, expected list, got {type(raw)}')

            result = []
            for item in raw:
                if isinstance(item, dict):
                    result.append(AiMovie.from_dict(item))
                elif isinstance(item, str):
                    # Skip empty strings
                    if item.strip():
                        result.append(AiMovie(title=item, match_score=0))
                elif item is None:
                    # Skip None values
                    continue
                else:
                    raise AiResponseError(f'AI returned invalid item type, expected dict or str, got {type(item)}')

            return result

        except AiResponseError:
            raise

        except Exception as exc:
            raw_preview = getattr(response, 'content', None)
            if raw_preview and len(raw_preview) > 0:
                raw_preview = getattr(raw_preview[0], 'text', str(raw_preview))[:500]
            else:
                raw_preview = str(response)[:500]
            logger.warning('AI parse failed: exc=%s raw_preview=%r', exc, raw_preview)
            raise AiResponseError(f'Failed to parse AI response: {exc}') from exc

    @property
    def client(self) -> OpenAI:
        if self._client is None:
            self._client = OpenAI(api_key=settings.OPENAI_API_KEY)
        return self._client


class SearchFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = find_movie_system_prompt
    DEFAULT_MAX_TOKENS = 4096
    MAX_EMPTY_LENGTH_RETRIES = 2

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_SEARCH_MODEL', 'gpt-5')
        super().__init__(model=model, **kwargs)


class RecommendationFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = recommendations_system_prompt
    DEFAULT_MAX_TOKENS = 4096
    MAX_RETRIES = 2

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_MODEL', 'gpt-5-mini')
        super().__init__(model=model, **kwargs)

    def find_movies(self, user_prompt: str) -> list[AiMovie]:
        for attempt in range(self.MAX_RETRIES):
            result = super().find_movies(user_prompt)
            if result:
                return result
            if attempt < self.MAX_RETRIES - 1:
                logger.warning('Recommendation AI returned empty (attempt %d/%d), retrying', attempt + 1, self.MAX_RETRIES)
        return result


class TopMoviesFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = top_movies_system_prompt
    DEFAULT_MAX_TOKENS = 4096

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_MODEL', 'gpt-5-mini')
        super().__init__(model=model, **kwargs)
