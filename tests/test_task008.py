import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task008_baseline import validate_translation_setup


class Task008TranslationValidationTests(unittest.TestCase):
    def test_required_translation_docs_and_rules_exist(self):
        result = validate_translation_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("technical_terms", result["translation_rules"])
        self.assertIn("proper_names", result["translation_rules"])


if __name__ == "__main__":
    unittest.main()
