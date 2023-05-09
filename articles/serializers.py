from rest_framework import serializers
from articles.models import Article, Comment

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