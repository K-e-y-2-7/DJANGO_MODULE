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


class Products(models.Model):
    name = models.CharField(max_length=180)
    price = models.DecimalField(default=1.0)
    image = models.ImageField(blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=0)

    description = models.TextField()
    shortdesc = description[:40]
 
    class Meta:
        ordering = ["name, price"]
        verbose_name_plural = "Products"

    def __str__(self):
        return f'Product {self.name}, quantity {self.quantity_in_stock} \n \
        {self.shortdesc} price{self.price}'



