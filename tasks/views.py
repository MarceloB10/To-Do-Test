from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse


class TaskViewSet(viewsets.ViewSet):

    @extend_schema(
        summary="Retrieve all tasks",
        responses={200: TaskSerializer(many=True)},
    )
    def list(self, request):
        """Retrieve all tasks."""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Create a new task",
        request=TaskSerializer,
        responses={201: TaskSerializer},
    )
    def create(self, request):
        """Create a new task."""
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Retrieve a task by ID",
        responses={200: TaskSerializer, 404: OpenApiResponse(description="Not Found")},
    )
    def retrieve(self, request, id=None):
        """Retrieve a task by ID."""
        task = get_object_or_404(Task, pk=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @extend_schema(
        summary="Update a task by ID",
        request=TaskSerializer,
        responses={200: TaskSerializer, 404: OpenApiResponse(description="Not Found")},
    )
    def update(self, request, id=None):
        """Update a task by ID."""
        task = get_object_or_404(Task, pk=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Delete a task by ID",
        responses={
            204: OpenApiResponse(description="No Content"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
    def destroy(self, request, id=None):
        """Delete a task by ID."""
        task = get_object_or_404(Task, pk=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
