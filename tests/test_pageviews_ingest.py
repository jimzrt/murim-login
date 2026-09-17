import unittest

from tools.pageviews_ingest import classify, normalize_path, parse_event


def _event(uri: str, ua: str = "Mozilla/5.0", status: int = 200) -> dict:
    return {
        "ts": 1700000000.5,
        "status": status,
        "duration": 0.012,
        "size": 1234,
        "request": {
            "method": "GET",
            "uri": uri,
            "client_ip": "1.2.3.4",
            "headers": {"User-Agent": [ua], "Referer": ["https://murim-login.com/"]},
        },
    }


class PageviewsIngestTest(unittest.TestCase):
    def test_chapter_and_home_paths(self):
        self.assertEqual(classify(normalize_path("/chapter/160/")), 160)
        self.assertEqual(classify(normalize_path("/murim-login/chapter/7")), 7)
        self.assertIsNone(classify(normalize_path("/")))
        self.assertIs(classify(normalize_path("/sw.js")), False)

    def test_parse_filters(self):
        row = parse_event(_event("/chapter/160/?x=1"), "salt")
        self.assertEqual(row[1], 160)
        self.assertEqual(row[2], "/chapter/160/")
        self.assertIsNone(parse_event(_event("/chapter/160/", "Googlebot"), "salt"))
        self.assertIsNone(parse_event(_event("/pagefind/index.js"), "salt"))
        self.assertIsNone(parse_event(_event("/chapter/160/", status=404), "salt"))
