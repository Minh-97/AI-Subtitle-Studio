import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task002_baseline import validate_environment_setup


class Task002EnvironmentValidationTests(unittest.TestCase):
    def test_required_environment_docs_exist_and_are_valid(self):
        result = validate_environment_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("pytest", result["dependencies"])


if __name__ == "__main__":
    unittest.main()
