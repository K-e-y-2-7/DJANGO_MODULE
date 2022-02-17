from django.contrib.auth.models import AbstractUser
from django.db import models


# Кастомный юзер
class MyUser(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)
    wallet = models.DecimalField(default=0.0, decimal_places=2, max_digits=15)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name_plural = 'MyUser'

    def __str__(self) -> str:
        return f'Name - {self.first_name},surname - {self.last_name}'


class Products(models.Model):
    name = models.CharField(max_length=180)
    price = models.DecimalField(default=1.0, decimal_places=2, max_digits=15)
    image = models.ImageField(blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=0)

    description = models.TextField()

    class Meta:
        ordering = ['name', 'price']
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product {self.name}, price{self.price}'


class Purchases(models.Model):
    customer = models.ForeignKey(
        MyUser, on_delete=models.DO_NOTHING, related_name='myuser'
    )
    product = models.ManyToManyField(Products, through="ProductPurchase")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Purchases'


class ProductPurchase(models.Model):
    """Product-Purchase M2M implementation"""

    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Returns(models.Model):
    purchase = models.ForeignKey(
        Purchases, on_delete=models.CASCADE, related_name='purchases'
    )
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['purchase', 'time']
        verbose_name_plural = 'Returns'

    def __str__(self):
        return f'Return purchase: {self.purchase}, at time: {self.time}'
