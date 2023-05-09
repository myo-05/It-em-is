from django.urls import path
from articles import views

urlpatterns = [
    # 게시글 url
    # 게시글 path url??
    # 댓글 url
    # 게시글 상세페이지에 comment CRUD
    path('<int:article_id>/comment/', views.CommentView.as_view(), name='comment_view'),
]