from django.db import models
from django.contrib.auth.models import User
from authapp.models import *
from consultentapp.models import ConsultentProfile
import uuid
# Create your models here.


class ConsultBooking(models.Model):
    booking_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consultent = models.ForeignKey(ConsultentProfile, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True)
    meeting_time = models.TimeField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.booking_user.username
    