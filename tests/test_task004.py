import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task004_baseline import validate_input_handling_setup


class Task004InputHandlingValidationTests(unittest.TestCase):
    def test_required_input_handling_docs_and_rules_exist(self):
        result = validate_input_handling_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("video", result["input_types"])
        self.assertIn("audio", result["input_types"])
        self.assertIn("metadata", result["metadata_fields"])


if __name__ == "__main__":
    unittest.main()
