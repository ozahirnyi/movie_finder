from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from django.conf import settings
from django.test import SimpleTestCase

from movie.ai_find_movie import FindMovieAiClient


class FindMovieAiClientTests(SimpleTestCase):
    def test_returns_empty_list_when_prompt_too_long(self):
        with patch('movie.ai_find_movie.Client.count_tokens', return_value=settings.MAX_PROMPT_TOKENS_LENGTH + 1):
            client = FindMovieAiClient('an extremely long prompt')
            result = client.find_movies()

        self.assertEqual(result, [])

    @patch('movie.ai_find_movie.Client.count_tokens', return_value=10)
    @patch('movie.ai_find_movie.Anthropic')
    def test_parse_response_into_ai_movies(self, mock_anthropic, _):
        fake_response = SimpleNamespace(content=[SimpleNamespace(text='["Shrek", "Shrek 2"]')])
        fake_client = MagicMock()
        fake_client.messages.create.return_value = fake_response
        mock_anthropic.return_value = fake_client

        client = FindMovieAiClient('family animation')
        result = client.find_movies()

        self.assertEqual([movie.title for movie in result], ['Shrek', 'Shrek 2'])
        fake_client.messages.create.assert_called_once()

    @patch('movie.ai_find_movie.Client.count_tokens', return_value=10)
    @patch('movie.ai_find_movie.Anthropic')
    def test_find_movies_raises_wrapped_exception(self, mock_anthropic, _):
        fake_client = MagicMock()
        fake_client.messages.create.side_effect = RuntimeError('boom')
        mock_anthropic.return_value = fake_client

        client = FindMovieAiClient('prompt')

        with self.assertRaises(Exception) as exc:
            client.find_movies()

        self.assertIn('Error while finding movies', str(exc.exception))

    def test_parse_response_error_path(self):
        fake_response = SimpleNamespace(content=[SimpleNamespace(text='not-json')])

        with self.assertRaises(Exception) as exc:
            FindMovieAiClient._parse_response(fake_response)

        self.assertIn('Error while parsing response', str(exc.exception))
