from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()


# Create your models here.
