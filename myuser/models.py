from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils

#Кастомный юзер
class MyUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True) 
    avatar = models.ImageField(blank=True, null=True)
    wallet = models.DecimalField(default= 0.0, decimal_places=2, max_digits=15)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name_plural = 'MyUser'

    def __str__(self) -> str:
        return  f'Name - {self.first_name}, surname - {self.last_name}'

