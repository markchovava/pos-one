from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
  email = models.EmailField(unique=True)
  code = models.CharField(max_length=255, null=True, blank=True)
  access_level = models.IntegerField(null=True, blank=True)
  phone_number = models.CharField(max_length=255, null=True, blank=True)
  address = models.TextField(null=True, blank=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)


class AppInfo(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=255, null=True, blank=True)
  address = models.TextField(max_length=255, null=True, blank=True)
  email = models.CharField(max_length=255, null=True, blank=True)
  phone_number = models.CharField(max_length=255, null=True, blank=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self) -> str:
      return self.name

  class Meta:
      ordering = ['name','created_at']

