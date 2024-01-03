# from .models import CustomUser
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
import random

class InterestSeralizer(serializers.ModelSerializer):
    class Meta:
        model = InterestModel
        fields = '__all__'

class UserInfoSerailzer(serializers.ModelSerializer):
    interests = InterestSeralizer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'interests', 'first_name', 'last_name', 'phone_number', 'is_profile_completed']
    def update(self, instance, validated_data):
        interests_data = validated_data.pop('interests', [])
        instance = super().update(instance, validated_data)

        # Assuming interests is a ManyToManyField in CustomUser model
        instance.interests.set([])  # Clear existing interests
        for interest_data in interests_data:
            interest, created = InterestModel.objects.get_or_create(**interest_data)
            instance.interests.add(interest)

        return instance
    

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
