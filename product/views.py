from django.shortcuts import render
from rest_framework import viewsets
from product import serializers
from product import models
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    """handles adding products"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (IsAuthenticated, )


