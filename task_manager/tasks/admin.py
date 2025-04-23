from django.contrib import admin

from task_manager.tasks.models import Task


@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'executor', 'status')
    search_fields = ('name', 'creator__username')
    list_filter = ('status',)
