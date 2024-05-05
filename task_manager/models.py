from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from company_task_tracker import settings


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return {self.name}


class Task(models.Model):
    CHOICES = [
        ("urgent", "Urgent"),
        ("important", "Important"),
        ("normal", "Normal"),
        ("low", "Low"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=55, choices=CHOICES, default="low")
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="workers",
    )

    def __str__(self):
        return (
            f"{self.name}, {self.task_type},\n"
            f"{self.priority}, {self.is_completed}\n"
            f"{self.description}"
        )


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return {self.name}


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="positions",
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return (
            f"{self.username}\n"
            f"{self.first_name} {self.last_name} - {self.position}"
        )
