import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, company_name, password=None):
        if not email:
            raise ValueError("User must have an email address.")
        if not company_name:
            raise ValueError("User must have a company name.")

        user = self.model(email=self.normalize_email(email),
                          company_name=company_name,
                          )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, company_name, password):
        user = self.create_user(email=self.normalize_email(email),
                                company_name=company_name,
                                password=password,
                                )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Organization(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    company_name = models.CharField(max_length=30)

    # The following fields are required for every custom User model
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"Subscription for {self.organization}"
