# from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework import serializers
class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password_again = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_again']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password_again = validated_data.get('password_again')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email allready exists")
        if password == password_again:
            user = User(username=username)
            user.set_password(password)
            user.save()
            return user