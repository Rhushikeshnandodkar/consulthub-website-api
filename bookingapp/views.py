from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utlils import get_service, create_google_meet

import datetime
# Create your views here.
class BookMeetingApiView(CreateAPIView):
    queryset = ConsultBooking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(booking_user=self.request.user)
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

class UserBookingsApiView(ListAPIView):
    queryset = ConsultBooking.objects.all()
    serializer_class = ShowBookingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        print(user)
        user_bookings = ConsultBooking.objects.filter(booking_user=user)
        return user_bookings


