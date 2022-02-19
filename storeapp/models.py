from django.db import models
import myuser.models
import django.utils
# Create your models here.


class Goods(models.Model):
    name = models.CharField(max_length=180)
    price = models.DecimalField(default=1.0, decimal_places=2, max_digits=15)
    image = models.ImageField(blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=0)

    description = models.TextField()
    
    class Meta:
        ordering = ['name', 'price']
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    customer = models.ForeignKey(myuser.models.MyUser,\
        on_delete=models.DO_NOTHING, related_name='myuser')
    goods = models.ManyToManyField(Goods, through='GoodsCount',)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['customer', 'time']
        verbose_name_plural = 'Purchase'

    def __str__(self):
        return f'{self.customer},'


class GoodsCount(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,\
        related_name='goods')
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE,\
        related_name='order')
    goods_count = models.IntegerField(default=1)


class Return(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['purchase', 'time']
        verbose_name_plural = 'Return'

    def __str__(self):
        return f'{self.purchase},'