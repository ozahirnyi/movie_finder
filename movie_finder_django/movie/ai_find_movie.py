import json

from anthropic import Anthropic, Client
from django.conf import settings

from .dataclasses import AiMovie
from .prompts import find_movies_prompt


class FindMovieAiClient:

    def __init__(self, expression: str):
        self.expression = expression
        self._client = None
        self.base_parameters = {
            'model': 'claude-3-5-sonnet-20240620',
            'max_tokens': 1024,
        }

    def find_movies(self) -> list[AiMovie]:
        if self.count_tokens() > settings.MAX_PROMPT_TOKENS_LENGTH:
            return []
        response = self.client.messages.create(
            **self.base_parameters,
            messages=[
                {
                    'role': 'user',
                    'content': [
                        {
                            'type': 'text',
                            'text': find_movies_prompt.format(REQUIREMENTS=self.expression),
                        },
                    ],
                },
            ],
        )
        return self._parse_response(response)

    def count_tokens(self) -> int:
        return Client().count_tokens(find_movies_prompt.format(REQUIREMENTS=self.expression))

    @staticmethod
    def _parse_response(response) -> list[AiMovie]:
        ai_movies = []
        for data in json.loads(response.content[0].text):
            ai_movies.append(AiMovie(**data))
        return ai_movies

    @property
    def client(self):
        if not self._client:
            self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        return self._client
