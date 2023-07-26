from .models import Account
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ['phone', 'name', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ['phone', 'password']


