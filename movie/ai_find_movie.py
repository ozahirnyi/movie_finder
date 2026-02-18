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
        logger.info('AI response: raw_prefix=%r', raw_text[:500] if raw_text else '')
        wrapped = SimpleNamespace(content=[SimpleNamespace(text=raw_text or '[]')])
        return self._parse_response(wrapped)

    def count_tokens(self, user_prompt: str) -> int:
        full_text = (self.system_prompt or '') + '\n' + user_prompt
        return _count_tokens_openai(full_text, self.model)

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

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_SEARCH_MODEL', 'gpt-5')
        super().__init__(model=model, **kwargs)


class RecommendationFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = recommendations_system_prompt

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_MODEL', 'gpt-5-mini')
        super().__init__(model=model, **kwargs)


class TopMoviesFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = top_movies_system_prompt

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'OPENAI_AI_MODEL', 'gpt-5-mini')
        super().__init__(model=model, **kwargs)
