from django.shortcuts import render, redirect
from rest_framework import viewsets
from users import serializers
from users import models
from rest_framework.permissions import IsAuthenticated
from .permissions import UpdateOwnProfile

#forms
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CustomUserSerializer
    queryset = models.CustomUser.objects.all()
    permission_classes = (IsAuthenticated, UpdateOwnProfile)


def registerpage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User has been created')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
        return render(request, 'users/home.html')

      