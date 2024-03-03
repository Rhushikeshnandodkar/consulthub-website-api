from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register-user', RegisterAPIView.as_view()),
    path('is-auth', IsAuth.as_view()),
    path('generate-token', GoogleLogin.as_view(), name="generate-token"),
    path('user-info', UserInfoApiView.as_view(), name="user-info"),
    path('validate-otp', ValidateOptApiView.as_view(), name="user-info"),
    path('google-signup', GoogleSignupnApiView.as_view(), name="google-signup"),
    path('google-login', GoogleLoginApiView.as_view(), name="google-login"),
    path('get-interests', GetInteresetsApiView.as_view(), name="get-interest"),
    path('get-otp', GenerateOtpApiView.as_view(), name="get-otp"),
    path('verify-otp', VerifyOtpApiView.as_view(), name="verify-otp"),



]