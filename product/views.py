from django.shortcuts import render
from rest_framework import viewsets
from product import serializers
from .models import Product
from rest_framework.permissions import IsAuthenticated
from django.views import View
from .forms import AddPostForm
from django.contrib import messages
<<<<<<< HEAD
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
=======


class ProductViewSet(viewsets.ModelViewSet):
    """handles adding products"""

    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
>>>>>>> refs/remotes/origin/master


class ProductView(View):
    """To show the products in homepage"""

    def get(self, request):
        name = (
            Product.objects.filter()
        )  # filtering objects by name to show products to users
        malewear = Product.objects.filter(clothes_type="MW")
        femalewear = Product.objects.filter(clothes_type="FW")

        context = {"name": name, "malewear": malewear, "femalewear": femalewear}
        return render(request, "app/home.html", context)


class ProductDetailView(View):
    """To display the details of the product"""

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        name = Product.objects.filter()

        context = {"product": product, "name": name}
        return render(request, "app/productdetail.html", context)


@method_decorator(login_required, name='dispatch')
class AddPostFormView(View):
    """Allows users to add new post"""
<<<<<<< HEAD
    
    def get(self, request):
        form = AddPostForm()
        context = {'form': form}
        return render(request, 'app/addpost.html', context)
=======

    def get(self, request):
        form = AddPostForm()
        context = {"form": form}
        return render(request, "app/addpost.html", context)
>>>>>>> refs/remotes/origin/master

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # commit false prevents data from writing into database
            updated_form = form.save(commit=False)
            # fetching user from request and assigning it to posted_by field
            updated_form.posted_by = request.user
<<<<<<< HEAD
            updated_form.contact_number = request.user.phone
            messages.success(request, 'product has been posted!')
            # saving new valid form
            updated_form.save()
            form = AddPostForm()
            
        context = {'form': form}
        return render(request, 'app/addpost.html', context)


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    """lets user delete their posts"""
    model = Product
    template_name = 'app/delete_post.html'
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    """lets user edit and update their posts"""
    model = Product
    template_name = 'app/edit_post.html'
    fields = ['name', 'brand', 'description', 'price']
    success_url = "/"


def searchproduct(request):
    """lets user search for products"""
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'app/search.html', {'searched':searched, 'products':products})
    else:
        return render(request, 'app/search.html', {})






=======
            # saving new valid form
            updated_form.save()
            messages.success(request, "product has been posted!")
        context = {"form": form}
        return render(request, "app/addpost.html", context)
>>>>>>> refs/remotes/origin/master
