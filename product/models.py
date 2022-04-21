from django.db import models
from djmoney.models.fields import MoneyField
from cms import commons
from users.models import CustomUser
from django.conf import settings


# Create your models here.
class Product(models.Model):
    """database model for adding clothes"""
    
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='NPR')
    photo = models.ImageField(upload_to='image')
    size = models.CharField(choices=commons.SIZES, max_length=1, blank=True)
    clothes_type = models.CharField(choices=commons.CLOTHES_TYPES, max_length=12, blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
    