from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'  # when run: python manage.py createsuperuser this field authentication user.

    REQUIRED_FIELDS = ['full_name']  # when make superuser this field question


    def __str__(self):
        return f'{self.full_name} email is {self.email} '
    

    def has_perm(self, perm, obj=None):  # permission user to admin panel
        return True

    def has_module_perms(self, app_label):  # permission user module
        return True

    @property
    def is_staff(self):  # user is superuser? if is_admin:True ,  User can be is_staff
        return self.is_admin
