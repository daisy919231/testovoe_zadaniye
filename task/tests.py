from django.test import TestCase
from task.models import Task
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.is_completed, False)


class TaskAPITest(APITestCase):
    def setUp(self):
        Task.objects.all().delete()

    def test_get_all_tasks(self):
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        response = self.client.get(reverse("all-tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 2)
