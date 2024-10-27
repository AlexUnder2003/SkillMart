from django.db import models
from django.contrib.auth.models import User

class PurchasedCourse(models.Model):
    """
    Модель, связывающая пользователей с курсами.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.course.title}"
