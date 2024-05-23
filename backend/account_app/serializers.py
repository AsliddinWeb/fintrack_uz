from django.contrib.auth.models import User
from rest_framework import serializers

# Jwt
from rest_framework_simplejwt.tokens import RefreshToken

# Local
from .models import Account

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # Create an Account for the user
        Account.objects.create(user=user, name=f"{user.first_name} {user.last_name}", balance=0)
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            refresh_token = RefreshToken(self.token)
            refresh_token.blacklist()
        except Exception as e:
            self.fail('bad_token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

class AccountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['image']
        extra_kwargs = {
            'image': {'required': False},
        }

class AccountUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['user']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Update user fields
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        return instance
