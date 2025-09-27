import json

from anthropic import Anthropic
from django.conf import settings

from .dataclasses import AiMovie
from .system_prompts import find_movie_system_prompt


class FindMovieAiClient:
    def __init__(self, expression: str):
        self.expression = expression
        self._client = None
        self.base_parameters = {
            'model': 'claude-sonnet-4-20250514',
            'max_tokens': 2048,
            'system': find_movie_system_prompt,
        }

    def find_movies(self) -> list[AiMovie]:
        if self.count_tokens() > settings.MAX_PROMPT_TOKENS_LENGTH:
            return []
        try:
            response = self.client.messages.create(
                **self.base_parameters,
                messages=[
                    {
                        'role': 'user',
                        'content': [
                            {
                                'type': 'text',
                                'text': self.expression,
                            },
                        ],
                    },
                ],
            )
        except Exception as e:
            raise Exception(f'Error while finding movies: {e}')
        return self._parse_response(response)

    def count_tokens(self) -> int:
        response = self.client.messages.count_tokens(
            model=self.base_parameters['model'],
            messages=[
                {
                    'role': 'user',
                    'content': [
                        {
                            'type': 'text',
                            'text': self.expression,
                        }
                    ],
                }
            ],
        )
        return response.input_tokens

    @staticmethod
    def _parse_response(response) -> list[AiMovie]:
        try:
            ai_movies = []
            for data in json.loads(response.content[0].text):
                ai_movies.append(AiMovie(data))
            return ai_movies
        except Exception as e:
            raise Exception(f'Error while parsing response: {e} | content: {response.content[0].text}')

    @property
    def client(self):
        if not self._client:
            self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        return self._client
