from django.test import SimpleTestCase

from movie.ai_resolve import (
    normalize_title,
    pick_best_imdb_candidate,
    title_similarity,
    title_variants,
)
from movie.dataclasses import AiMovie, ImdbMovie


class TitleNormalizeTests(SimpleTestCase):
    def test_normalize_title_strips_punctuation(self):
        self.assertEqual(normalize_title('The Matrix: Reloaded'), 'the matrix reloaded')

    def test_title_variants_include_shortened_forms(self):
        variants = title_variants('The Dark Knight: IMAX')
        self.assertIn('The Dark Knight', variants)
        self.assertIn('Dark Knight', variants)

    def test_title_similarity_prefers_close_match(self):
        self.assertGreater(title_similarity('The Matrix', 'Matrix'), 0.9)
        self.assertLess(title_similarity('The Matrix', 'Inception'), 0.5)


class PickBestImdbCandidateTests(SimpleTestCase):
    def test_prefers_year_match(self):
        candidates = [
            ImdbMovie('The Batman', 'tt1', '', '2022', 'movie'),
            ImdbMovie('Batman', 'tt2', '', '1989', 'movie'),
        ]
        best = pick_best_imdb_candidate(candidates, 'Batman', '1989')
        self.assertEqual(best.imdb_id, 'tt2')

    def test_returns_none_when_similarity_too_low(self):
        candidates = [ImdbMovie('Totally Different', 'tt1', '', '2020', 'movie')]
        self.assertIsNone(pick_best_imdb_candidate(candidates, 'The Matrix', '1999'))


class AiMovieYearTests(SimpleTestCase):
    def test_from_dict_parses_year(self):
        movie = AiMovie.from_dict({'title': 'The Matrix', 'year': 1999, 'match_score': 90})
        self.assertEqual(movie.year, '1999')
