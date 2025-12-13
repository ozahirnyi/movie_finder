import json
from typing import Optional

from anthropic import Anthropic
from django.conf import settings

from .dataclasses import AiMovie
from .system_prompts import find_movie_system_prompt, recommendations_system_prompt, top_movies_system_prompt


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
            raise Exception(f'Error while finding movies: {exc}') from exc
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
                raise TypeError(f'Expected list from AI response, got {type(raw)}')

            return [AiMovie.from_dict(item) for item in raw]
        except TypeError:
            raise

        except Exception as exc:
            raise Exception(f'Error while parsing response: {exc} | content: {response.content[0].text}') from exc

    @property
    def client(self) -> Anthropic:
        if self._client is None:
            self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        return self._client


class SearchFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = find_movie_system_prompt


class RecommendationFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = recommendations_system_prompt


class TopMoviesFindMovieAiClient(FindMovieAiClient):
    SYSTEM_PROMPT = top_movies_system_prompt
