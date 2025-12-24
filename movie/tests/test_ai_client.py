from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
from django.conf import settings
from django.core.exceptions import BadRequest
from django.test import SimpleTestCase

from movie.ai_find_movie import (
    FindMovieAiClient,
    RecommendationFindMovieAiClient,
    SearchFindMovieAiClient,
)
from movie.dataclasses import AiMovie
from movie.errors import AiResponseError
from movie.services import MovieService
from movie.system_prompts import find_movie_system_prompt, recommendations_system_prompt


class FindMovieAiClientTests(SimpleTestCase):
    def test_returns_empty_list_when_prompt_too_long(self):
        with patch.object(
            SearchFindMovieAiClient,
            'count_tokens',
            return_value=settings.MAX_PROMPT_TOKENS_LENGTH + 1,
        ):
            client = SearchFindMovieAiClient()
            result = client.find_movies('an extremely long prompt')

        self.assertEqual(result, [])

    @patch.object(SearchFindMovieAiClient, 'count_tokens', return_value=10)
    @patch('movie.ai_find_movie.Anthropic')
    def test_parse_response_into_ai_movies(self, mock_anthropic, _):
        fake_response = SimpleNamespace(content=[SimpleNamespace(text='[{"title": "Shrek", "match_score": 10}, {"title": "Shrek 2"}]')])
        fake_client = MagicMock()
        fake_client.messages.create.return_value = fake_response
        mock_anthropic.return_value = fake_client

        client = SearchFindMovieAiClient()
        result = client.find_movies('family animation')

        self.assertEqual([(m.title, m.match_score) for m in result], [('Shrek', 10), ('Shrek 2', 0)])
        fake_client.messages.create.assert_called_once()

    def test_ai_movie_from_dict_invalid_type(self):
        with pytest.raises(TypeError):
            AiMovie.from_dict('Shrek')

    @patch.object(SearchFindMovieAiClient, 'count_tokens', return_value=10)
    @patch('movie.ai_find_movie.Anthropic')
    def test_find_movies_raises_wrapped_exception(self, mock_anthropic, _):
        fake_client = MagicMock()
        fake_client.messages.create.side_effect = RuntimeError('boom')
        mock_anthropic.return_value = fake_client

        client = SearchFindMovieAiClient()

        with self.assertRaises(Exception) as exc:
            client.find_movies('prompt')

        self.assertIn('Error while finding movies', str(exc.exception))

    def test_parse_response_raises_ai_response_error_when_not_list(self):
        fake_response = SimpleNamespace(content=[SimpleNamespace(text='{"title": "Shrek"}')])

        with pytest.raises(AiResponseError) as exc:
            SearchFindMovieAiClient._parse_response(fake_response)

        self.assertIn('expected list', str(exc.value))

    def test_parse_response_error_path(self):
        fake_response = SimpleNamespace(content=[SimpleNamespace(text='not-json')])

        with self.assertRaises(Exception) as exc:
            FindMovieAiClient._parse_response(fake_response)

        self.assertIn('Failed to parse AI response', str(exc.exception))

    def test_get_movies_from_ai_handles_ai_response_error(self):
        """Перевірка обробки AiResponseError в сервісному шарі"""
        mock_ai_client = MagicMock()
        mock_ai_client.find_movies.side_effect = AiResponseError('Invalid AI response')

        service = MovieService(ai_client=mock_ai_client)

        with pytest.raises(BadRequest) as exc_info:
            service.get_movies_from_ai('some expression')

        assert 'AI service returned an invalid response' in str(exc_info.value)
        mock_ai_client.find_movies.assert_called_once_with('some expression')

    @patch('movie.ai_find_movie.Anthropic')
    def test_count_tokens_calls_messages_api(self, mock_anthropic):
        mock_messages = MagicMock()
        mock_messages.count_tokens.return_value = SimpleNamespace(input_tokens=42)
        mock_client = MagicMock(messages=mock_messages)
        mock_anthropic.return_value = mock_client

        client = SearchFindMovieAiClient()
        tokens = client.count_tokens('prompt')

        mock_messages.count_tokens.assert_called_once()
        self.assertEqual(tokens, 42)

    @patch('movie.ai_find_movie.Anthropic')
    def test_client_property_caches_instance(self, mock_anthropic):
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        client = SearchFindMovieAiClient()

        first = client.client
        second = client.client

        self.assertIs(first, second)
        mock_anthropic.assert_called_once_with(api_key=settings.ANTHROPIC_API_KEY)

    def test_subclasses_define_prompts(self):
        self.assertEqual(SearchFindMovieAiClient().system_prompt, find_movie_system_prompt)
        self.assertEqual(
            RecommendationFindMovieAiClient().system_prompt,
            recommendations_system_prompt,
        )
