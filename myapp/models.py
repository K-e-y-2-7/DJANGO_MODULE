import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

#Кастомный юзер
class MyUser(AbstractUser):
    '''Custom user'''
    birth_date = models.DateField() 
    avatar = models.ImageField(blank=True, null=True)
    wallet = models.DecimalField(default= 0.0)

    class Meta:
        ordering = ["first_name, last_name"]
        verbose_name_plural = "User"

    def __str__(self) -> str:
        return  f"Username - {self.username}, name - {self.first_name}, \
surname - {self.last_name}, age - {datetime.timezone.now() - self.birth_date}"





