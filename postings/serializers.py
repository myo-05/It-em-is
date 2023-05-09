from .models import Postings
import datetime
from rest_framework import serializers


class PostingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email

    def get_likes_count(self, obj):
        return obj.likes.count()
        
    class Meta:
        model = Postings
        fields = ['user','id','title','content','image','likes_count',]

class PostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postings 
        fields = ['title','content','image']
        
class PostingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postings 
        fields = ['title','content','image']