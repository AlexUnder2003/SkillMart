from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    """
    Модель пользователя.
    """

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения.
        """
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
