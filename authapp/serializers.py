# from .models import CustomUser
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password_again = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_again', 'phone_number']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password_again = validated_data.get('password_again')
        phone = validated_data.get('phone_number')

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("email allready exists")
        if password == password_again:
            user = CustomUser(username=username, email=email, phone_number=phone)
            user.set_password(password)
            user.save()
            return user