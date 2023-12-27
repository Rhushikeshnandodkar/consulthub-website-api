from rest_framework import serializers
from .models import *
from django.conf import settings

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
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = ConsultentProfile
        fields = ['id', 'consultent_name', 'title', 'total_meetings', 'average_rating', 'rate', 'profile_image', 'languages', 'category']

    def get_average_rating(self, obj):
        return obj.average_rating()

class ConsultentDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    languages = LanguageSerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = ConsultentProfile
        fields = '__all__'
        
    def get_average_rating(self, obj):
        print(obj.average_rating())
        return obj.average_rating()

class ConsultentReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = ReviewModel
        fields = '__all__'