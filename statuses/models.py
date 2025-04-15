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




# Create your models here.
