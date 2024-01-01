# from .models import CustomUser
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
import random
class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password_again = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_again', 'phone_number']

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        password_again = validated_data.get('password_again')

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("email allready exists")
        if password == password_again:
            user = CustomUser(username=email, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            serializers.ValidationError("passwords are not equal")