from django.test import TestCase

from tasks.models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task", description="Test description", completed=False
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)

    def test_task_str(self):
        task = Task.objects.create(
            title="Test Task", description="Test description", completed=False
        )
        self.assertEqual(str(task), "Test Task")
