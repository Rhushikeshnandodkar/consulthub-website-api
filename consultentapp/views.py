from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.decorators import APIView
from rest_framework import filters
from bookingapp.serializers import *
from bookingapp.models import *
from rest_framework.response import Response
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
    
class FetchLanguagesApiView(ListAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer

class FetchCategoryApiView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class FilterConsultentsApiView(ListAPIView):
    serializer_class = ConsultentListSerializer
    queryset = ConsultentProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['consultent_name', 'title']
    
    def get_queryset(self):
        language = self.request.query_params.get('language', None)
        category = self.request.query_params.get('category', None)
        if language and category==None:
            language_id = LanguageModel.objects.get(language_field=language)
            queryset = ConsultentProfile.objects.filter(languages=language_id)
            return queryset
        if category and language == None:
            category_id = CategoryModel.objects.get(cateogry_field=category)
            queryset = ConsultentProfile.objects.filter(category=category_id)
            return queryset

class FetchReviewsApiView(ListAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ConsultentReviewSerializer
    lookup_field = 'rid'
    def get_queryset(self):
        review_id = self.kwargs['rid']
        print(review_id)
        c_profile = ConsultentProfile.objects.get(id=review_id)
        queryset = ReviewModel.objects.filter(consultent_profile=c_profile)
        return queryset