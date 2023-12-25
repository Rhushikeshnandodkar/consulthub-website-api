from rest_framework import serializers
from .models import *
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultBooking
        fields = '__all__'

        