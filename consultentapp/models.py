from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultent_name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-pics')
    age = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(CategoryModel)
    description = models.TextField(null=True, blank=True)
    total_meetings = models.IntegerField(null=True, blank=True)
    meetings_cancelled = models.IntegerField(null=True, blank=True)
    average_rating = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    languages = models.ManyToManyField(LanguageModel)
    rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.consultent_name
