import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task003_baseline import validate_configuration_setup


class Task003ConfigurationValidationTests(unittest.TestCase):
    def test_required_configuration_docs_and_files_exist(self):
        result = validate_configuration_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("input_dir", result["parameters"])
        self.assertIn("output_dir", result["parameters"])
        self.assertIn("subtitle_duration_seconds", result["parameters"])


if __name__ == "__main__":
    unittest.main()
