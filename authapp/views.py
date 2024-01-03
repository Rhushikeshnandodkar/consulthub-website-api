from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth.models import User
from rest_framework import status
from .models import *
from django.contrib.auth import authenticate
from rest_framework.generics import *
import requests
from rest_framework import filters
class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            serializer_data = {
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':serializer.data
            }
            return Response(serializer_data)
        return Response(serializer.errors)
    
class GoogleSignupnApiView(APIView):
    def post(self, request):
        access_token = request.data.get('access_token')
        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json',               
            }
            google_api_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
            params = {'access_token': access_token}
            try:
                response = requests.get(google_api_url, params=params, headers=headers)
                response.raise_for_status()
                user_info = response.json()
                email = user_info.get('email')
                first_name = user_info.get('given_name')
                last_name = user_info.get('family_name')

                if CustomUser.objects.filter(email=email).exists():
                    message = {"message":"email allready exists"}
                    return Response(message, status=status.HTTP_409_CONFLICT)
                else:
                    user = CustomUser.objects.create(email=email, username=email, first_name=first_name, last_name=last_name)
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    serializer_data = {
                        'refresh':str(refresh),
                        'access':str(refresh.access_token),
                        'user':user_info
                    }
                    return Response(serializer_data, status=status.HTTP_200_OK)
            except requests.exceptions.RequestException as err:
                print(err)
                return Response({"message": "something went wrong", "err": err})
        else:
            return Response({"message":"please provide token"})
        
class GoogleLoginApiView(APIView):
    def post(self, request):
        access_token = request.data.get('access_token')
        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json',               
            }
            google_api_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
            params = {'access_token': access_token}
            try:
                response = requests.get(google_api_url, params=params, headers=headers)
                response.raise_for_status()
                user_info = response.json()
                email = user_info.get('email')
                first_name = user_info.get('given_name')
                last_name = user_info.get('family_name')

                if CustomUser.objects.filter(email=email).exists():
                    user = CustomUser.objects.get(email=email)
                    refresh = RefreshToken.for_user(user)
                    serializer_data = {
                        'refresh':str(refresh),
                        'access':str(refresh.access_token),
                        'user':user_info
                    }
                    return Response(serializer_data, status=status.HTTP_200_OK)
                else:
                    message = {"message": "User with given Email not exist"}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)
            except requests.exceptions.RequestException as err:
                print(err)
                return Response({"message": "something went wrong", "err": err})
        else:
            return Response({"message":"please provide token"})
class ValidateOptApiView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_get = request.data.get('otp')
        print(otp_get)

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            user = CustomUser.objects.get(phone_number=phone_number)
            if user.otp == otp_get:
                user.is_active = True
                user.save()
                return Response({"message": "otp varified"})
            else:
                user = CustomUser.objects.get(phone_number=phone_number)
                user.delete()
                return Response({"message" : "otp is wrong please try again"})
        else:
            return Response({"message" : "user does not exists"})

    
class IsAuth(APIView):
    serializer_class = UserRegisterSerializer
    def get(self, request, format=None):
        print(request.user)
        return Response({"username": request.user.username})
    
class GoogleLogin(APIView):
    def post(self, request):
        token = {'idToken': request.data.get('id_token')}
        print(token)
        idinfo = id_token.verify_oauth2_token(token['idToken'], google_requests.Request(), '1027394913320-j3uue43cnlj1mrge46ctgohkpo1okjhn.apps.googleusercontent.com')
        print(idinfo)
        user = User.objects.filter(email=idinfo['email']).first()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            })
        else:
            user = User.objects.create(username=idinfo['email'], email=idinfo['email'])
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': "user created succesfully",
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            })
        
class UserInfoApiView(APIView):
    serializer_class = UserInfoSerailzer
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserInfoSerailzer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {"message":"user is not authenticated"}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
    def patch(self, request, format=None):
        if request.user.is_authenticated:
            # id = request.data.get('id')
            model = CustomUser.objects.get(id=request.user.id)
            print(model)
            serializer = UserInfoSerailzer(model, data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.errors)
                return Response({"message": "give real data"})
        messsage = {"message": "please login"}
        return Response(messsage, status=status.HTTP_401_UNAUTHORIZED)
    
class GetInteresetsApiView(ListAPIView):
    serializer_class = InterestSeralizer
    queryset = InterestModel.objects.all()
    search_fields = ['interest']
    filter_backends = (filters.SearchFilter,)
