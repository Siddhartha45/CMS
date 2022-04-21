from django.shortcuts import render, redirect
from rest_framework import viewsets
from users import serializers
from users import models
from rest_framework.permissions import IsAuthenticated
from .permissions import UpdateOwnProfile
from django.views import View

#forms
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CustomUserSerializer
    queryset = models.CustomUser.objects.all()
    permission_classes = (UpdateOwnProfile, )


class RegisterFormView(View):
    """form for registering new users"""
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'User has been registered successfully!')
            form.save()
            form = RegisterForm()   #After form is saved empty form is returned to the user
            #return redirect('login')
            
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)





def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

# def login(request):
#  return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')




      