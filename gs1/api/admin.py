from django.contrib import admin
from .models import Product, Items

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'color', 'image', 'price']

# admin.site.register(Product, ProductAdmin)

class ItemsAdmin(admin.ModelAdmin):
    list_display=['product', 'quantity']

admin.site.register(Product, ProductAdmin)
admin.site.register(Items, ItemsAdmin)