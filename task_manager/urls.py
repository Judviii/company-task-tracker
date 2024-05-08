from django.urls import path

from .views import (
    index,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerUpdateView,
    WorkerListView,
    WorkerDetailView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"
    ),
]

app_name = "task_manager"
