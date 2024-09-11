from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tasks.models import Task


class TaskTests(TestCase):

    def setUp(self):
        # Crear una instancia del APIClient para realizar solicitudes
        self.client = APIClient()

        # Crear algunas tareas para probar
        self.task1 = Task.objects.create(
            title="Test Task 1", description="Test description 1", completed=False
        )
        self.task2 = Task.objects.create(
            title="Test Task 2", description="Test description 2", completed=True
        )

    def test_get_all_tasks(self):
        # Realizar solicitud GET para obtener todas las tareas
        response = self.client.get(reverse("task-list"))

        # Asegurarse de que la respuesta es 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Comprobar que obtenemos dos tareas
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        # Datos de la nueva tarea
        data = {
            "title": "New Task",
            "description": "New task description",
            "completed": False,
        }

        # Realizar solicitud POST para crear una nueva tarea
        response = self.client.post(reverse("task-list"), data)

        # Comprobar que la respuesta es 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar que la tarea fue creada
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, "New Task")

    def test_get_task_by_id(self):
        # Realizar solicitud GET para obtener una tarea por su ID
        response = self.client.get(reverse("task-detail", args=[self.task1.id]))

        # Comprobar que la respuesta es 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que los datos de la tarea son correctos
        self.assertEqual(response.data["title"], self.task1.title)

    def test_update_task(self):
        # Nuevos datos para actualizar la tarea
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True,
        }

        # Realizar solicitud PUT para actualizar la tarea
        response = self.client.put(reverse("task-detail", args=[self.task1.id]), data)

        # Comprobar que la respuesta es 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que la tarea fue actualizada
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Updated Task")

    def test_delete_task(self):
        # Realizar solicitud DELETE para eliminar una tarea
        response = self.client.delete(reverse("task-detail", args=[self.task1.id]))

        # Comprobar que la respuesta es 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificar que la tarea fue eliminada
        self.assertEqual(Task.objects.count(), 1)
