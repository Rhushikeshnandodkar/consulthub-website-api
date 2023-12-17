from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = '__all__'
        
class ConsultentListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    languages = LanguageSerializer(many=True)
    class Meta:
        model = ConsultentProfile
        fields = ['consultent_name', 'title', 'total_meetings', 'average_rating', 'rate', 'profile_image', 'languages', 'category']

class ConsultentDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    languages = LanguageSerializer(many=True)
    class Meta:
        model = ConsultentProfile
        fields = '__all__'