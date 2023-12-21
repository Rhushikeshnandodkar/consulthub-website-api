from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
class BookMeetingApiView(CreateAPIView):
    queryset = ConsultBooking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            return Response({"data" : serializer.data})
        else:
            return Response({"message":"please enter valid data"})

