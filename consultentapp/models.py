from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from authapp.models import *
from django.db.models import Avg
# Create your models here.
class CategoryModel(models.Model):
    cateogry_field = models.CharField(max_length=200)
    def __str__(self):
        return self.cateogry_field

class LocationModel(models.Model):
    location_field = models.CharField(max_length=200)
    def __str__(self):
        return self.location_field

class LanguageModel(models.Model):
    language_field = models.CharField(max_length=200)
    def __str__(self):
        return self.language_field
    
class ConsultentProfile(models.Model):
    user = models.ForeignKey('Consultents', on_delete=models.CASCADE)
    consultent_name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-pics')
    age = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(InterestModel)
    linkedin_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total_meetings = models.IntegerField(null=True, blank=True)
    meetings_cancelled = models.IntegerField(null=True, blank=True)
    average_rate = models.FloatField(null=True, blank=True, default=0)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    languages = models.ManyToManyField(LanguageModel)
    rate = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.consultent_name
    def average_rating(self):
        return ReviewModel.objects.filter(consultent_profile=self).aggregate(Avg('rating'))
class ConsultentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_consultent=True)
class Consultents(CustomUser):
    objects = ConsultentManager()
    class Meta:
        proxy = True
   
class ReviewModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consultent_profile = models.ForeignKey(ConsultentProfile, on_delete=models.CASCADE)
    review_title = models.TextField(max_length=600, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

class SpeakersModel(models.Model):
    user = models.ForeignKey('Speakers', on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-pics')
    age = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(CategoryModel)
    linkedin_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total_events = models.IntegerField(null=True, blank=True)
    events_cancelled = models.IntegerField(null=True, blank=True)
    average_rate = models.FloatField(null=True, blank=True, default=0)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    languages = models.ManyToManyField(LanguageModel)
    rate = models.IntegerField(null=True, blank=True)
class SpeakerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_influhencer=True)
class Speakers(CustomUser):
    objects = SpeakerManager()
    class Meta:
        proxy = True

class Event(models.Model):
    speaker_name = models.CharField(max_length=200, null=True, blank=True)
    speaker_tagline = models.CharField(max_length=800, null=True, blank=True)
    achievement_one = models.CharField(max_length=800, null=True, blank=True)
    subachievement_one = models.CharField(max_length=800, null=True, blank=True)
    achievement_two = models.CharField(max_length=800, null=True, blank=True)
    subachievement_two = models.CharField(max_length=800, null=True, blank=True)
    achievement_three = models.CharField(max_length=800, null=True, blank=True)
    subachievement_three = models.CharField(max_length=800, null=True, blank=True)
    achievement_four = models.CharField(max_length=800, null=True, blank=True)
    subachievement_four = models.CharField(max_length=800, null=True, blank=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    profile_image = models.ImageField(upload_to='profile-pics', null=True, blank=True)
    upcomming = models.BooleanField(default=False)
    insta_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.speaker_name
    
class Community_cateogry(models.Model):
    cat = models.CharField(max_length=300)
    def __str__(self):
        return self.cat
    

class Community(models.Model):
    community_name = models.CharField(max_length=300)
    community_image = models.ImageField(upload_to='community-pics', null=True, blank=True)
    members = models.IntegerField()
    community_desc = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    cateogry = models.ForeignKey(Community_cateogry, on_delete=models.CASCADE)

    def __str__(self):
        return self.community_name

