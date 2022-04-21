from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'description', 'price', 'clothes_type', 'posted_by', 'contact_number']
