import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task011_baseline import validate_timing_alignment_setup


class Task011TimingAlignmentValidationTests(unittest.TestCase):
    def test_required_timing_alignment_docs_and_rules_exist(self):
        result = validate_timing_alignment_setup(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_files"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertIn("sync_rules", result["timing_rules"])
        self.assertIn("time_offset_handling", result["timing_rules"])
        self.assertIn("pause_handling", result["timing_rules"])


if __name__ == "__main__":
    unittest.main()
