from django.db import models
from djmoney.models.fields import MoneyField
from cms import commons
#from users.models import CustomUser

# Create your models here.
class Product(models.Model):
    """database model for adding clothes"""
    
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='NPR')
    photo = models.ImageField()
    size = models.CharField(choices=commons.SIZES, max_length=1, blank=True)
    #posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    