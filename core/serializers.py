from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'address', 'code', 'access_level']


class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'code', 'address', 'access_level']



