import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.task_implementations import execute_task


class TaskImplementationTests(unittest.TestCase):
    def test_tasks_1_to_30_generate_real_artifacts(self):
        for task_id in range(1, 31):
            with self.subTest(task_id=task_id):
                result = execute_task(task_id, ROOT)
                self.assertTrue(result["implemented"], msg=result.get("error", "task failed"))
                artifact_path = Path(result["artifact_path"])
                self.assertTrue(artifact_path.exists(), msg=f"artifact missing for task {task_id}")
                self.assertTrue(result.get("summary"))
                self.assertEqual(result["task_id"], f"{task_id:03d}")


if __name__ == "__main__":
    unittest.main()
