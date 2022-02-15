from django.contrib.auth.models import AbstractUser
from django.db import models

#Кастомный юзер
class MyUser(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)

