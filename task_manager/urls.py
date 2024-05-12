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
    TaskDetailView,
    toggle_assign_to_task,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    PositionListView,
    PositionCreateView,
    PositionDetailView,
    PositionUpdateView,
    PositionDeleteView,
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
    path(
        "tasks/<int:pk>/detail", TaskDetailView.as_view(), name="task-detail"
    ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="task-toggle-assign"
    ),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task-type/<int:pk>/detail/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail",
    ),
    path(
        "task-type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task-type/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path("position/", PositionListView.as_view(), name="position-list"),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "position/<int:pk>/detail/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
]

app_name = "task_manager"
