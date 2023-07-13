from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import User, AppInfo


class UserCreateSerializer(BaseUserCreateSerializer):
  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'address', 'code', 'access_level']


class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'code', 'address', 'access_level']

class UserAllSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'code', 'address', 'access_level']


class AppInfoSerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   user = UserSerializer(read_only=True)
   class Meta:
      model = AppInfo
      fields = ['id','user_id', 'user', 'name', 'phone_number', 'address', 'email']