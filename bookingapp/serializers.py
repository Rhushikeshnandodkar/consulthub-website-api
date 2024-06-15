from rest_framework import serializers
from .models import *
from consultentapp.serializers import ConsultentListSerializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultBooking
        fields = '__all__'
        read_only_fields = ['booking_user']


class ShowBookingSerializer(serializers.ModelSerializer):
    consultent = ConsultentListSerializer()
    class Meta:
        model = ConsultBooking
        fields = '__all__'

        