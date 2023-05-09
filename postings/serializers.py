from .models import Postings, Comment
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

class CommentSerializer(serializers.ModelSerializer):
    # 댓글 조회 시리얼라이저-직렬화
    # class Meta:
        model = Comment
    pass

class CommentSerializer(serializers.ModelSerializer):
    # 댓글 생성 시리얼라이저-직렬화, 검증까지
    # class Meta:
        model = Comment

    pass