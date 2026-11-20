import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task010_baseline import validate_subtitle_formatting_setup


class Task010SubtitleFormattingValidationTests(unittest.TestCase):
    def test_required_subtitle_formatting_docs_and_rules_exist(self):
        result = validate_subtitle_formatting_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("segmenting_rules", result["formatting_rules"])
        self.assertIn("line_break_rules", result["formatting_rules"])
        self.assertIn("max_chars_per_line", result["formatting_rules"])


if __name__ == "__main__":
    unittest.main()
