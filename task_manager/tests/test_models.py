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

        self.assertIn(
            Permission.objects.get(codename="add_task"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="change_task"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="delete_task"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="view_task"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="add_position"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="change_position"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="delete_position"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="view_position"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="add_tasktype"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="change_tasktype"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="delete_tasktype"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="view_tasktype"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="add_worker"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="change_worker"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="delete_worker"),
            default_permissions
        )
        self.assertIn(Permission.objects.get(
            codename="view_worker"),
            default_permissions
        )
