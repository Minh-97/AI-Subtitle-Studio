import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task007_baseline import validate_transcript_qa_setup


class Task007TranscriptQAValidationTests(unittest.TestCase):
    def test_required_transcript_qa_docs_and_rules_exist(self):
        result = validate_transcript_qa_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("completeness", result["quality_criteria"])
        self.assertIn("duplication", result["quality_criteria"])
        self.assertIn("major_error", result["error_categories"])


if __name__ == "__main__":
    unittest.main()
