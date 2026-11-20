import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task_backlog import validate_task_documents


class TaskBacklogValidationTests(unittest.TestCase):
    def test_all_task_documents_follow_the_required_structure(self):
        result = validate_task_documents(ROOT)

        self.assertTrue(result["is_valid"], msg=result["errors"])
        self.assertEqual(result["missing_tasks"], [])
        self.assertEqual(result["missing_sections"], [])
        self.assertEqual(result["tasks_checked"], 30)

    def test_task_documents_are_present_for_every_expected_task(self):
        result = validate_task_documents(ROOT)

        self.assertEqual(len(result["task_files"]), 30)
        self.assertIn("tasks/Task001.md", result["task_files"])
        self.assertIn("tasks/Task030.md", result["task_files"])


if __name__ == "__main__":
    unittest.main()
