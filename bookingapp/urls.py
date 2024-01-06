from django.urls import path, include
from .views import *
urlpatterns = [
  path('book-meet', BookMeetingApiView.as_view()),
  path('user-booking',  UserBookingsApiView.as_view()),
]