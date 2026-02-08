import json
import logging
from typing import Optional

from anthropic import Anthropic
from django.conf import settings

from .dataclasses import AiMovie
from .errors import AiResponseError
from .system_prompts import find_movie_system_prompt, recommendations_system_prompt, top_movies_system_prompt

logger = logging.getLogger(__name__)


class FindMovieAiClient:
    DEFAULT_MODEL = 'claude-sonnet-4-20250514'
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
        self._client: Optional[Anthropic] = None

    def find_movies(self, user_prompt: str) -> list[AiMovie]:
        if self.count_tokens(user_prompt) > settings.MAX_PROMPT_TOKENS_LENGTH:
            return []
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=self.system_prompt,
                messages=self._build_messages(user_prompt),
            )
        except Exception as exc:
            logger.exception('AI request failed: %s', exc)
            raise Exception(f'Error while finding movies: {exc}') from exc
        raw_text = response.content[0].text if response.content else ''
        logger.info('AI response: raw_prefix=%r', raw_text[:500] if raw_text else '')
        return self._parse_response(response)

    def count_tokens(self, user_prompt: str) -> int:
        response = self.client.messages.count_tokens(
            model=self.model,
            messages=self._build_messages(user_prompt),
        )
        return response.input_tokens

    def _build_messages(self, user_prompt: str) -> list[dict[str, object]]:
        return [
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': user_prompt,
                    },
                ],
            },
        ]

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
    def client(self) -> Anthropic:
        if self._client is None:
            self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        return self._client


class SearchFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = find_movie_system_prompt

    def __init__(self, *, model: str | None = None, **kwargs) -> None:
        model = model or getattr(settings, 'ANTHROPIC_AI_SEARCH_MODEL', FindMovieAiClient.DEFAULT_MODEL)
        super().__init__(model=model, **kwargs)


class RecommendationFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = recommendations_system_prompt


class TopMoviesFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = top_movies_system_prompt
