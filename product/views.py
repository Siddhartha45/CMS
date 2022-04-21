from django.shortcuts import render
from rest_framework import viewsets
from product import serializers
from .models import Product
from rest_framework.permissions import IsAuthenticated
from django.views import View
from .forms import AddPostForm
from django.contrib import messages


class ProductViewSet(viewsets.ModelViewSet):
    """handles adding products"""
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )


class ProductView(View):
    """To show the products in homepage"""
    def get(self, request):
        name = Product.objects.filter() #filtering objects by name to show products to users
        malewear = Product.objects.filter(clothes_type='MW')
        femalewear = Product.objects.filter(clothes_type='FW')
        
        context = {'name': name, 'malewear': malewear, 'femalewear': femalewear}
        return render(request, 'app/home.html', context)


class ProductDetailView(View):
    """To display the details of the product"""
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        name = Product.objects.filter()

        context = {'product': product, 'name':name}
        return render(request, 'app/productdetail.html', context)


class AddPostFormView(View):
    """Allows users to add new post"""
    def get(self, request):
        form = AddPostForm()
        context = {'form': form}
        return render(request, 'app/addpost.html', context)

    def clean_posted_by(self):
        data = self.cleaned_data['posted_by']
        data = self.request.user
        print("Cleaning Dataa")
        return data

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'product has been posted!')
            form.save()
        context = {'form': form}
        return render(request, 'app/addpost.html', context)
