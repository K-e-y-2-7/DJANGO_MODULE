from django.contrib import admin
import storeapp.models
# Register your models here.

@admin.register(storeapp.models.Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity_in_stock', 'description']
    list_filter = ['name', 'price', 'quantity_in_stock' ]


@admin.register(storeapp.models.Purchase) 
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'time']
    list_filter = ['customer', 'time']


@admin.register(storeapp.models.GoodsCount) 
class GoodsCountAdmin(admin.ModelAdmin):
    list_display = ['goods', 'purchase', 'goods_count']
    list_filter = ['goods', 'purchase', 'goods_count']


@admin.register(storeapp.models.Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ['purchase', 'time']
    list_filter = ['purchase', 'time']