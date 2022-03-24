from rest_framework import serializers
from product import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializes product object"""
    class Meta:
        model = models.Product
        fields = '__all__'