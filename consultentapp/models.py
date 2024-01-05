from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consultent_name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-pics')
    age = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(CategoryModel)
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
    
    
class ReviewModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consultent_profile = models.ForeignKey(ConsultentProfile, on_delete=models.CASCADE)
    review_title = models.TextField(max_length=600, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
