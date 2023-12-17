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