from django.contrib import admin
from .models import Category,Brand,Product,Product_Image
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Product_Image)