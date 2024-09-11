from django.test import TestCase
from tasks.serializers import TaskSerializer


class TaskSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            "title": "Test Task",
            "description": "Test description",
            "completed": False,
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], data["title"])
        self.assertEqual(serializer.validated_data["description"], data["description"])
        self.assertEqual(serializer.validated_data["completed"], data["completed"])

    def test_invalid_data(self):
        data = {"title": "", "description": "Test description", "completed": False}
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
