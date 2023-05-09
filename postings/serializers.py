from .models import Postings
import datetime
from rest_framework import serializers


class PostingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
        
    class Meta:
        model = Postings
        fields = ['user','id','title','content','image']

class PostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postings 
        fields = ['title','content','image']
        
class PostingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postings 
        fields = ['title','content','image']