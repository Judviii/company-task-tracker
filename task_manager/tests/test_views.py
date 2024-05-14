from django.test import TestCase
from django.urls import reverse
from task_manager.models import TaskType, Task, Position
from django.contrib.auth import get_user_model


HOME_PAGE_URL = reverse("task-manager:index")
TASK_URL = reverse("task_manager:task-list")
TASK_TYPE_URL = reverse("task_manager:task-type-list")
POSITION_URL = reverse("task_manager:position-list")
WORKER_URL = reverse("task_manager:worker-list")
User = get_user_model()


class PublicIndexTest(TestCase):
    def test_login_required(self):
        res = self.client.get(HOME_PAGE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIndexTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test34534",
        )
        self.client.force_login(self.user)

    def test_retrieve_index(self):
        response = self.client.get(HOME_PAGE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "base.html"
        )


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test_password"
        )
        self.client.force_login(self.user)

    def test_retrieve_worker(self):
        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "task_manager/worker_list.html"
        )

    def test_create_worker(self):
        position = Position.objects.create(name="Manager")
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "position": position.id,
            "first_name": "John",
            "last_name": "Doe",
        }
        self.client.post(reverse("task_manager:worker-create"), data=form_data)
        new_user = User.objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position, position)


class PublicTaskTypeTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTypeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test34534",
        )
        self.client.force_login(self.user)

    def test_retrieve_tasktype(self):
        TaskType.objects.create(
            name="Q&A",
        )
        response = self.client.get(TASK_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "task_manager/tasktype_list.html"
        )


class PublicPositionTest(TestCase):
    def test_login_required(self):
        response = self.client.get(POSITION_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test34534",
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(
            name="Manager",
        )
        response = self.client.get(POSITION_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "task_manager/position_list.html"
        )


class PublicTaskTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test34534",
        )
        self.client.force_login(self.user)

    def test_retrieve_task(self):
        task_type = TaskType.objects.create(
            name="Q&A",
        )
        Task.objects.create(
            name="Test name",
            description="Test description",
            deadline="2024-12-31T23:59:59",
            task_type=task_type,
            is_completed=False,
            priority="normal",

        )
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "task_manager/task_list.html"
        )
