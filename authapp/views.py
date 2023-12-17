from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
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