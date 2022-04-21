from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'phone', 'address']
