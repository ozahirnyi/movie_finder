from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from movie.trailer import (
    _pick_youtube_video_key,
    lookup_tmdb_trailer_video_id,
    lookup_trailer_video_id,
)


class PickYoutubeVideoKeyTests(SimpleTestCase):
    def test_prefers_official_trailer(self):
        videos = [
            {"site": "YouTube", "type": "Teaser", "key": "teaser-key", "official": True},
            {"site": "YouTube", "type": "Trailer", "key": "trailer-key", "official": True},
            {"site": "YouTube", "type": "Trailer", "key": "other-trailer", "official": False},
        ]
        self.assertEqual(_pick_youtube_video_key(videos), "trailer-key")

    def test_ignores_non_youtube_videos(self):
        videos = [
            {"site": "Vimeo", "type": "Trailer", "key": "vimeo-key", "official": True},
        ]
        self.assertIsNone(_pick_youtube_video_key(videos))


class LookupTmdbTrailerVideoIdTests(SimpleTestCase):
    @override_settings(TMDB_API_KEY="")
    def test_returns_none_when_tmdb_key_missing(self):
        self.assertIsNone(lookup_tmdb_trailer_video_id("tt0133093"))

    @override_settings(TMDB_API_KEY="tmdb-key")
    @patch("movie.trailer._fetch_tmdb_videos")
    @patch("movie.trailer.requests.get")
    def test_returns_youtube_key_from_tmdb(self, mock_get, mock_fetch_videos):
        find_response = mock_get.return_value
        find_response.ok = True
        find_response.json.return_value = {
            "movie_results": [{"id": 603}],
            "tv_results": [],
        }
        mock_fetch_videos.return_value = [
            {"site": "YouTube", "type": "Trailer", "key": "abc123xyz", "official": True},
        ]

        self.assertEqual(lookup_tmdb_trailer_video_id("tt0133093"), "abc123xyz")
        mock_get.assert_called_once()

    @override_settings(TMDB_API_KEY="tmdb-key")
    def test_returns_none_for_invalid_imdb_id(self):
        self.assertIsNone(lookup_tmdb_trailer_video_id("invalid"))


class LookupTrailerVideoIdTests(SimpleTestCase):
    @patch("movie.trailer.lookup_youtube_trailer_video_id", return_value="youtube-id")
    @patch("movie.trailer.lookup_tmdb_trailer_video_id", return_value=None)
    def test_falls_back_to_youtube(self, _mock_tmdb, _mock_youtube):
        self.assertEqual(
            lookup_trailer_video_id("The Matrix", "1999", "tt0133093"),
            "youtube-id",
        )

    @patch("movie.trailer.lookup_youtube_trailer_video_id")
    @patch("movie.trailer.lookup_tmdb_trailer_video_id", return_value="tmdb-id")
    def test_uses_tmdb_before_youtube(self, _mock_tmdb, mock_youtube):
        self.assertEqual(
            lookup_trailer_video_id("The Matrix", "1999", "tt0133093"),
            "tmdb-id",
        )
        mock_youtube.assert_not_called()
