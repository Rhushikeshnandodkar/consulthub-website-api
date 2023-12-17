from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.decorators import APIView
from rest_framework import filters
from bookingapp.serializers import *
from bookingapp.models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ConsultentsListApiView(ListAPIView):
    serializer_class = ConsultentListSerializer
    queryset = ConsultentProfile.objects.all()

class ConsultentDetailApiView(RetrieveAPIView):
    serializer_class = ConsultentDetailSerializer
    queryset = ConsultentProfile.objects.all()
    lookup_field = "id"

class ConsultentSearchApiView(ListAPIView):
    search_fields = ['consultent_name', 'title']
    filter_backends = (filters.SearchFilter,)
    queryset = ConsultentProfile.objects.all()
    serializer_class = ConsultentDetailSerializer

class YourBookingsApiView(ListAPIView):
    queryset = ConsultBooking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        print(user)
        profile = ConsultentProfile.objects.get(user=user)
        bookings = ConsultBooking.objects.filter(consultent=profile)
        return bookings
