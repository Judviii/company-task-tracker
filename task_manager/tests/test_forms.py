from django.contrib.auth import get_user_model
from django.test import TestCase
from task_manager.models import Position, TaskType
from task_manager.forms import (
    WorkerCreationForm,
    TaskForm,
    WorkerSearchForm,
    TaskSearchForm,
    TaskTypeSearchForm,
    PositionSearchForm,
)


class WorkerCreationTest(TestCase):
    def setUp(self):
        position = Position.objects.create(name="Manager")
        self.valid_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "position": position.id,
            "first_name": "John",
            "last_name": "Doe",
        }

    def test_worker_creation_form_with_position_first_last_name_valid(self):
        form = WorkerCreationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())


class TaskFormTestCase(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.position = Position.objects.create(name="Test Position")

        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
        )

        self.valid_data = {
            "name": "Test Task",
            "description": "Test description",
            "deadline": "2024-12-31T23:59:59",
            "is_completed": False,
            "priority": "normal",
            "task_type": self.task_type.id,
            "assignees": [self.user.id],
        }

    def test_task_form_valid(self):
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_task_form_save(self):
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertIsNotNone(task)
        self.assertEqual(task.name, self.valid_data["name"])
        self.assertEqual(task.description, self.valid_data["description"])
        self.assertEqual(task.deadline.strftime("%Y-%m-%dT%H:%M:%S"),
                         self.valid_data["deadline"])
        self.assertEqual(task.is_completed, self.valid_data["is_completed"])
        self.assertEqual(task.priority, self.valid_data["priority"])
        self.assertEqual(task.task_type.id, self.valid_data["task_type"])
        self.assertEqual(list(task.assignees.all()), [self.user])


class SearchFormsTest(TestCase):
    def test_worker_with_valid_data(self):
        form = WorkerSearchForm(data={"username": "Admin"})
        self.assertTrue(form.is_valid())

    def test_worker_with_invalid_data(self):
        form = WorkerSearchForm(data={"username": ""})
        self.assertTrue(form.is_valid())

    def test_task_with_valid_data(self):
        form = TaskSearchForm(data={"name": "a"})
        self.assertTrue(form.is_valid())

    def test_task_with_invalid_data(self):
        form = TaskSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())

    def test_task_type_with_valid_data(self):
        form = TaskTypeSearchForm(data={"name": "a"})
        self.assertTrue(form.is_valid())

    def test_task_type_with_invalid_data(self):
        form = TaskTypeSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())

    def test_position_with_valid_data(self):
        form = PositionSearchForm(data={"name": "a"})
        self.assertTrue(form.is_valid())

    def test_position_with_invalid_data(self):
        form = PositionSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())
