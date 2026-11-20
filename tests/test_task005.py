import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task005_baseline import validate_preprocessing_setup


class Task005PreprocessingValidationTests(unittest.TestCase):
    def test_required_preprocessing_docs_and_rules_exist(self):
        result = validate_preprocessing_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("audio", result["media_types"])
        self.assertIn("video", result["media_types"])
        self.assertIn("preprocessed_audio.wav", result["intermediate_outputs"])


if __name__ == "__main__":
    unittest.main()
