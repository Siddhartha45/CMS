from django.forms import ModelForm
from django import forms
from .models import CustomUser  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from cms import commons


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'gender', 'phone', 'address']
        widgets = {'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'name':forms.TextInput(attrs={'class':'form-control'}),
                    'gender':forms.Select(attrs={'class':'form-control'}),
                    'phone':forms.TextInput(attrs={'class':'form-control'}),
                    'address':forms.TextInput(attrs={'class':'form-control'}),
                    #'password':forms.PasswordInput(attrs={'class':'form-control'})
                  }


class LoginForm(AuthenticationForm):
    #email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class PwChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), 
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))


class PwResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=255, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))


class PwSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), 
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))