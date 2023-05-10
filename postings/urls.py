from django.urls import path
from postings import views

urlpatterns = [
    path('', views.PostingView.as_view(), name='posting_list'),
    path('<int:id>/', views.PostingDetail.as_view(), name='posting_detail'),
    path('<int:id>/likes/', views.LikeView.as_view(), name='like_view'),
    # 게시글 url
    path('<int:posting_id>/comment/', views.CommentView.as_view(), name='comment_view'),    # 해당 게시글의 댓글 조회, 생성
    path('comment/<pk>/', views.CommentDetailView.as_view(), name='comment_detail_view'),   # pk번 댓글의 수정, 삭제
    path('mypage/comment/', views.MyCommentView.as_view(), name='my_comments'), # 마이페이지의 내가 작성한 댓글 모두 보기
]