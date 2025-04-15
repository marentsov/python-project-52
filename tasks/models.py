from django.db import models

from labels.models import Label
from statuses.models import Status
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание задачи')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='Создатель',
        related_name='created_tasks',
    )
    executor = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='Исполнитель',
        related_name='assigned_tasks',
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.PROTECT,
        verbose_name='Статус',
        related_name='tasks',
    )
    label = models.ManyToManyField(
        to=Label,
        verbose_name='Метки',
        related_name='tasks',
        blank=True,
    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"Задача {self.title} || Исполнитель {self.creator.username}"
# Create your models here.
