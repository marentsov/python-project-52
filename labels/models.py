from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Метка')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'labels'
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
# Create your models here.
