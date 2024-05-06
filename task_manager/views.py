from django.shortcuts import render
from .models import Task, TaskType, Position


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    not_completed_tasks_count = Task.objects.filter(is_completed=False).count()

    context = {
        "num_tasks": num_tasks,
        "not_completed_tasks_count": not_completed_tasks_count,
    }

    return render(
        request, "task_manager/index.html",
        context=context
    )
