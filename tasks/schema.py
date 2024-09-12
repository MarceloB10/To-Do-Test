# tasks/schema.py
from typing import List

import strawberry
from strawberry import auto

from .models import Task


@strawberry.django.type(Task)
class TaskType:
    id: auto
    title: auto
    description: auto
    completed: auto


# Queries
@strawberry.type
class Query:
    all_tasks: List[TaskType] = strawberry.django.field()

    @strawberry.field
    def get_task(self, id: int) -> TaskType:
        return Task.objects.get(pk=id)


# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self, title: str, description: str, completed: bool) -> TaskType:
        task = Task.objects.create(
            title=title, description=description, completed=completed
        )
        return task

    @strawberry.mutation
    def update_task(
        self, id: int, title: str, description: str, completed: bool
    ) -> TaskType:
        task = Task.objects.get(pk=id)
        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        return task

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        task = Task.objects.get(pk=id)
        task.delete()
        return True


# Crear el esquema final combinando Query y Mutation
schema = strawberry.Schema(query=Query, mutation=Mutation)
