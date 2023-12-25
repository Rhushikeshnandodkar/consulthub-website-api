from django.db import models
from django.contrib.auth.models import User
from consultentapp.models import ConsultentProfile
# Create your models here.
class TimeSlotModel(models.Model):
    consultent
    day = models.DateField()
    time = models.TimeField()

class ConsultBooking(models.Model):
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultent = models.ForeignKey(ConsultentProfile, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    preferred_date = models.DateField()
    required_time = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.amount = self.required_time * self.consultent.rate
        print(self.amount)
        super(ConsultBooking, self).save(*args, **kwargs)   

    def __str__(self):
        return self.booking_user.username
    