from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from cms import commons


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, name, gender, phone, address, password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, address=address)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(choices=commons.GENDER_TYPES, max_length=7, default=commons.MALE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=60)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

