from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'
        verbose_name = 'Статуса'
        verbose_name_plural = 'Статусы'

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание задачи')
    status = models.ForeignKey(
        to=Status,
        on_delete=models.PROTECT,
        verbose_name='Статус',
        related_name='tasks',
    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# Create your models here.
