from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, TaskType, Worker, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(TaskType)

admin.site.register(Position)
