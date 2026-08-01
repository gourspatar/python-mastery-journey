import unittest
from todo_manager import TodoManager


class TestTodoManager(unittest.TestCase):

    def setUp(self):
        self.todo = TodoManager()

    def test_add_task(self):
        self.todo.add_task("Study Python")
        self.assertEqual(len(self.todo.tasks), 1)

    def test_add_multiple_tasks(self):
        self.todo.add_task("Python")
        self.todo.add_task("Git")
        self.assertEqual(len(self.todo.tasks), 2)

    def test_add_duplicate_task(self):
        self.todo.add_task("Python")

        with self.assertRaises(ValueError):
            self.todo.add_task("Python")

    def test_add_empty_task(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("")

    def test_remove_existing_task(self):
        self.todo.add_task("Python")
        self.todo.remove_task("Python")
        self.assertEqual(len(self.todo.tasks), 0)

    def test_remove_missing_task(self):
        with self.assertRaises(ValueError):
            self.todo.remove_task("Java")

    def test_mark_completed(self):
        self.todo.add_task("Python")
        self.todo.mark_completed("Python")
        self.assertTrue(self.todo.tasks[0]["completed"])

    def test_mark_completed_missing_task(self):
        with self.assertRaises(ValueError):
            self.todo.mark_completed("Java")

    def test_pending_tasks_initially(self):
        self.todo.add_task("Python")
        self.todo.add_task("Git")

        self.assertEqual(
            self.todo.pending_tasks(),
            ["Python", "Git"]
        )

    def test_pending_after_completion(self):
        self.todo.add_task("Python")
        self.todo.mark_completed("Python")

        self.assertEqual(self.todo.pending_tasks(), [])

    def test_remove_completed_task(self):
        self.todo.add_task("Python")
        self.todo.mark_completed("Python")
        self.todo.remove_task("Python")

        self.assertEqual(len(self.todo.tasks), 0)

    def test_task_is_in_list(self):
        self.todo.add_task("Python")
        self.assertIn("Python", self.todo.pending_tasks())

    def test_completed_task_not_pending(self):
        self.todo.add_task("Python")
        self.todo.mark_completed("Python")

        self.assertNotIn("Python", self.todo.pending_tasks())

    def test_add_three_tasks(self):
        self.todo.add_task("A")
        self.todo.add_task("B")
        self.todo.add_task("C")

        self.assertEqual(len(self.todo.tasks), 3)

    def test_all_completed(self):
        self.todo.add_task("A")
        self.todo.add_task("B")

        self.todo.mark_completed("A")
        self.todo.mark_completed("B")

        self.assertEqual(self.todo.pending_tasks(), [])


if __name__ == "__main__":
    unittest.main()