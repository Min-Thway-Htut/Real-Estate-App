from django.test import TestCase
from rest_framework import serializers
from .models import Rating

class RatingSerialier(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Rating
        exculde = ["updated_at", "pkid"]

    def get_rater(self, obj):
        return obj.rater.username
    
    def get_agent(self, obj):
        return obj.agent.user.username
    
    
