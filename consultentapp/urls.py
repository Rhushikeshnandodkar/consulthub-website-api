from django.urls import path, include
from .views import *
urlpatterns = [
    path('consultent-list', ConsultentsListApiView.as_view()),
    path('consultent-detail/<int:id>', ConsultentDetailApiView.as_view()),
    path('search-consultent', ConsultentSearchApiView.as_view()),
    path('your-bookings', YourBookingsApiView.as_view()),
    path('languages-list', FetchLanguagesApiView.as_view()),
    path('categories-list', FetchCategoryApiView.as_view()),
    path('filter-consultents', FilterConsultentsApiView.as_view()),
    path('filter-consultents', FilterConsultentsApiView.as_view()),
    path('fetch-reviews/<int:rid>',  FetchReviewsApiView.as_view()),
    path('speakers-list',  SpeakersListApiView.as_view()),
    path('post-reviews',  PubLishReviewApiView.as_view()),
    path('check-reviews',  ReviweValidityApiView.as_view()),
    path('upcomming-event',  EventApiView.as_view()),
    path('community',  FetchCommunityApiView.as_view()),


]