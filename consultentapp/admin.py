from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(CustomUser)
class ConsultentAdmin(admin.ModelAdmin):
    list_display = ['consultent_name', 'location']
admin.site.register(ConsultentProfile, ConsultentAdmin)
admin.site.register(LanguageModel)
admin.site.register(LocationModel)
admin.site.register(CategoryModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'consultent_profile', 'date']
admin.site.register(ReviewModel, ReviewAdmin)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['speaker_name', 'location']
admin.site.register(SpeakersModel, SpeakerAdmin)
admin.site.register(Event)
admin.site.register(Community)
admin.site.register(Community_cateogry)