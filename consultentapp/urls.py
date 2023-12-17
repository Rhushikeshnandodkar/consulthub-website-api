from django.urls import path, include
from .views import *
urlpatterns = [
    path('consultent-list', ConsultentsListApiView.as_view()),
    path('consultent-detail/<int:id>', ConsultentDetailApiView.as_view()),
    path('search-consultent', ConsultentSearchApiView.as_view()),
    path('your-bookings', YourBookingsApiView.as_view()),
]