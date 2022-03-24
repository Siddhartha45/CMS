from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm  


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'gender', 'phone', 'address']