from django.db import models
# from users.models import User

# Create your models here.

class Commet(models.Model):
    # 댓글 작성자 = 유저모델 FK로 받아오기
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # # 게시글에 댓글을 작성함으로 게시글도 FK로 받아오기
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 댓글 TextField
    Commet = models.TextField("댓글")   # verbosename="댓글"=> admin에서 댓글로 표시됨
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)