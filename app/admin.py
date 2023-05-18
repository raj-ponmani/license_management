from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Organization, Subscription

# Register your models here.

admin.site.register(get_user_model())
admin.site.register(Subscription)