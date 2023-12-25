from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth.models import User
from rest_framework import status
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
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                "username" : request.user.username,
                "email": request.user.email,
                "id": request.user.id
             }, status=status.HTTP_200_OK)
        else:
            message = {"message":"user is not authenticated"}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)