from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/')
    price=models.IntegerField()
    def __str__(self):
        return self.name


class Items(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity=models.IntegerField(default=1)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name