from django.shortcuts import render, redirect
from rest_framework import viewsets
from users import serializers
from users import models
from rest_framework.permissions import IsAuthenticated
from .permissions import UpdateOwnProfile
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
            #After form is saved empty form is returned to the user
            form = RegisterForm()   
            
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)






      