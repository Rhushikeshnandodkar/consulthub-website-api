from django.db import models
from django.contrib.auth.models import User
from consultentapp.models import ConsultentProfile
import uuid
# Create your models here.


class ConsultBooking(models.Model):
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultent = models.ForeignKey(ConsultentProfile, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return self.booking_user.username
    