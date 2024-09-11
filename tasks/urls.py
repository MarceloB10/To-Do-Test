from django.urls import path
from .views import TaskViewSet
from strawberry.django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path(
        "tasks/",
        TaskViewSet.as_view({"get": "list", "post": "create"}),
        name="task-list",
    ),
    path(
        "tasks/<int:id>/",
        TaskViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="task-detail",
    ),
    path("graphql/", GraphQLView.as_view(schema=schema, graphiql=True)),
]
