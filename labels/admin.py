from django.contrib import admin

from labels.models import Label


@admin.register(Label)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name",]
# Register your models here.
