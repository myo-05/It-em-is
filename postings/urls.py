from django.urls import path
from postings import views

urlpatterns = [
    path('', views.PostingView.as_view(), name='posting_list'),
    path('<str:id>/', views.PostingDetail.as_view(), name='posting_detail'),
    # 게시글 url
    # 게시글 path url??
    # 댓글 url
    # 게시글 상세페이지에 comment CRUD
    path('<int:article_id>/comment/', views.CommentView.as_view(), name='comment_view'),
]