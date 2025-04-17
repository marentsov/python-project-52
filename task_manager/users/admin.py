from django.contrib import admin
from task_manager.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name", "first_name"]
# Register your models here.
