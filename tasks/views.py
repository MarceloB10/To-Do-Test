import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse

# Get the logger for the 'tasks' app
logger = logging.getLogger("tasks")


class TaskViewSet(viewsets.ViewSet):

    @extend_schema(
        summary="Retrieve all tasks",
        responses={200: TaskSerializer(many=True)},
    )
    def list(self, request):
        logger.info("Retrieving all tasks.")
        tasks = Task.objects.all()
        logger.debug(f"{tasks.count()} tasks found.")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Create a new task",
        request=TaskSerializer,
        responses={201: TaskSerializer},
    )
    def create(self, request):
        logger.info("Creating a new task.")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            logger.info(f"Task created with ID: {task.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Task creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Retrieve a task by ID",
        responses={200: TaskSerializer, 404: OpenApiResponse(description="Not Found")},
    )
    def retrieve(self, request, id=None):
        logger.info(f"Retrieving task with ID: {id}")
        try:
            task = get_object_or_404(Task, pk=id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving task with ID: {id} - {e}")
            raise

    @extend_schema(
        summary="Update a task by ID",
        request=TaskSerializer,
        responses={200: TaskSerializer, 404: OpenApiResponse(description="Not Found")},
    )
    def update(self, request, id=None):
        logger.info(f"Updating task with ID: {id}")
        try:
            task = get_object_or_404(Task, pk=id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Task with ID: {id} updated successfully.")
                return Response(serializer.data)
            logger.error(f"Failed to update task with ID: {id} - {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating task with ID: {id} - {e}")
            raise

    @extend_schema(
        summary="Delete a task by ID",
        responses={
            204: OpenApiResponse(description="No Content"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
    def destroy(self, request, id=None):
        logger.info(f"Deleting task with ID: {id}")
        try:
            task = get_object_or_404(Task, pk=id)
            task.delete()
            logger.info(f"Task with ID: {id} deleted successfully.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting task with ID: {id} - {e}")
            raise
