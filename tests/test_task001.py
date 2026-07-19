import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task001_baseline import validate_project_docs


class Task001DocumentationValidationTests(unittest.TestCase):
    def test_required_docs_exist_and_are_valid(self):
        result = validate_project_docs(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertEqual(result["inconsistencies"], [])

    def test_project_name_is_consistent_across_core_docs(self):
        result = validate_project_docs(ROOT)

        self.assertIn("AI Subtitle Studio", result["project_name"])
        self.assertEqual(result["core_docs_checked"], 3)


if __name__ == "__main__":
    unittest.main()
