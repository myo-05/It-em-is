from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from postings.models import Article

# Create your views here.
class LikeView(APIView):
    def get(self, request,article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            # 유저가 좋아요 명단 안에 있을 때
            article.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)

    def post(self, request,article_id):
        pass