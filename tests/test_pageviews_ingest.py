import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.pageviews_ingest import classify, normalize_path, parse_event, query_counts


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

    def test_query_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "pageviews.db"
            conn = sqlite3.connect(db)
            conn.executescript(
                """
                CREATE TABLE pageviews (
                  id INTEGER PRIMARY KEY,
                  ts TEXT NOT NULL,
                  chapter INTEGER,
                  path TEXT NOT NULL,
                  status INTEGER NOT NULL,
                  ip_hash TEXT,
                  ua TEXT,
                  referer TEXT,
                  bytes INTEGER,
                  duration_ms INTEGER
                );
                INSERT INTO pageviews (ts, chapter, path, status) VALUES
                  ('2026-01-01T00:00:00Z', 160, '/chapter/160/', 200),
                  ('2026-01-01T00:01:00Z', 160, '/chapter/160/', 200),
                  ('2026-01-01T00:02:00Z', 161, '/chapter/161/', 200);
                """
            )
            conn.close()
            with patch("tools.pageviews_ingest.db_path", return_value=db):
                rows = query_counts([160, 161, 162])
            self.assertEqual(rows, [
                {"chapter": 160, "count": 2},
                {"chapter": 161, "count": 1},
                {"chapter": 162, "count": 0},
            ])
