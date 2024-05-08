from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Task, TaskType, Position, Worker


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


class WorkerListView(generic.ListView):
    model = Worker

    def get_queryset(self):
        queryset = Worker.objects.order_by("username")
        username = self.request.GET.get("username", "")
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class WorkerDetailView(generic.DetailView):
    model = Worker
    queryset = Worker.objects.all()


class WorkerCreateView(generic.CreateView):
    model = Worker


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    success_url = reverse_lazy("")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task-manager:index")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_manager/task_list.html"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task-manager:task-list")
