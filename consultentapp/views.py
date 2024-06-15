from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.decorators import APIView
from rest_framework import filters
from bookingapp.serializers import *
from bookingapp.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ConsultentsListApiView(ListAPIView):
    serializer_class = ConsultentListSerializer
    queryset = ConsultentProfile.objects.all()

class SpeakersListApiView(ListAPIView):
    serializer_class = SpeakerListSerailizer
    queryset = SpeakersModel.objects.all()

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
    queryset = InterestModel.objects.all()
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
            category_id = InterestModel.objects.get(interest=category)
            queryset = ConsultentProfile.objects.filter(category=category_id)
            return queryset
        
class PubLishReviewApiView(CreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ConsultentReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # customer = self.request.query_params.get('customer', None)
        consultent = self.request.query_params.get('consultent', None)
        booking = ConsultBooking.objects.filter(booking_user=request.user.id, consultent=consultent).exists()
        if booking:
            print(booking)
            booking_object = ConsultBooking.objects.filter(booking_user=request.user.id, consultent=consultent, is_paid=True).first()
            review = ReviewModel.objects.filter(user=request.user.id, consultent_profile=consultent).exists()
            if review:
                return Response({"message": "you have allready posted reivew"})
            else:
                if booking_object:
                    request.data['user'] = request.user.id 
                    request.data['consultent_profile'] = consultent
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    instance = serializer.save()
                    return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message":"first take consultetion"})
        else:
            return Response({"message": "book this consultent first"})
        
class ReviweValidityApiView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            consultent = self.request.query_params.get('consultent', None)
            booking = ConsultBooking.objects.filter(booking_user=request.user.id, consultent=consultent, is_paid=True).exists()
            review = ReviewModel.objects.filter(user=request.user.id, consultent_profile=consultent).exists()
            if booking:
                if review:
                    data = {
                        'can_post' : False
                    }
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'can_post' : True
                    }
                    return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'can_post' : False
                }
                return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "user not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

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
from django.core.exceptions import ObjectDoesNotExist
class EventApiView(APIView):
    def get(self, request):
        upcomming_event_exist = Event.objects.filter(upcomming=True).exists()
        if upcomming_event_exist:
            upcomming_event = Event.objects.filter(upcomming=True).first()
            serializer = EventSerializer(upcomming_event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"data does not exists"}, status=status.HTTP_204_NO_CONTENT)
        
class FetchCommunityApiView(ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer