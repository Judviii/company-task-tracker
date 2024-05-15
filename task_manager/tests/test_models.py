from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from task_manager.models import TaskType, Task, Position
from django.contrib.auth import get_user_model


class TaskTypeModelTests(TestCase):
    def test_manufacturer_str(self):
        tasktype = TaskType.objects.create(name="test")
        self.assertEqual(
            str(tasktype), tasktype.name
        )


class PositionModelTests(TestCase):
    def test_manufacturer_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(
            str(position), position.name
        )


class TaskModelTests(TestCase):
    def test_task_str(self):
        task_type = TaskType.objects.create(name="Test")
        task = Task(
            name="Test Task",
            description="Test description",
            task_type=task_type,
            is_completed=False,
            priority="normal",
        )
        self.assertEqual(
            str(task), (
                f"{task.name}, {task.task_type},\n"
                f"{task.priority}, {task.is_completed}\n"
                f"{task.description}"
            )
        )


class WorkerModelTests(TestCase):
    def test_driver_str(self):
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create(
            username="TEST",
            first_name="test",
            last_name="TeSt",
            position=position,
        )
        self.assertEqual(
            str(worker), (
                f"{worker.username}\n"
                f"{worker.first_name} {worker.last_name} - {worker.position}"
            )
        )

    def test_get_absolute_url(self):
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create(
            username="TEST",
            first_name="test",
            last_name="TeSt",
            position=position,
        )
        self.assertEqual(
            worker.get_absolute_url(),
            reverse("task-manager:worker-detail", kwargs={"pk": worker.pk}),
        )

    def test_get_default_permissions(self):
        position = Position.objects.create(name="test_position")
        worker = get_user_model().objects.create(
            username="test_user",
            first_name="Test",
            last_name="User",
            position=position,
        )
        default_permissions = worker.get_default_permissions()

        expected_codenames = [
            "add_task", "change_task", "delete_task", "view_task",
            "add_position", "change_position", "delete_position",
            "view_position", "add_tasktype", "change_tasktype",
            "delete_tasktype", "view_tasktype", "add_worker",
            "change_worker", "delete_worker", "view_worker",
        ]

        for codename in expected_codenames:
            self.assertIn(Permission.objects.get(codename=codename),
                          default_permissions,
                          msg=f"Missing permission: {codename}")
