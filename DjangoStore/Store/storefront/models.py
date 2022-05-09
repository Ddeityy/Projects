from django.db import models
from django.urls import *
from django.core.validators import MinValueValidator


class Material(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products', # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0)],
    )

    material = models.ManyToManyField(Material, through="ProductMaterial")
    
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])
    
    
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name.title()