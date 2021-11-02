from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
# Create your models here.


class User(AbstractBaseUser):

    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True)
    address = models.TextField(default="hi")
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['full_name', 'email', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

