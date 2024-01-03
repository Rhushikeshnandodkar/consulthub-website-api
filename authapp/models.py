from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    is_consultent = models.BooleanField(default=False)
    is_influhencer = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    interests = models.ManyToManyField("InterestModel")
    is_profile_completed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class InterestModel(models.Model):
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest
    
