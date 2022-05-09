from django.contrib import admin
from .models import Material, Product, Category, ProductMaterial

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(ProductMaterial)
# Register your models here.
