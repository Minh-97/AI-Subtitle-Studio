import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task006_baseline import validate_transcript_setup


class Task006TranscriptValidationTests(unittest.TestCase):
    def test_required_transcript_docs_and_rules_exist(self):
        result = validate_transcript_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("transcript_segments", result["transcript_fields"])
        self.assertIn("confidence", result["transcript_fields"])


if __name__ == "__main__":
    unittest.main()
