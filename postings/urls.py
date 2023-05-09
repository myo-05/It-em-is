from django.urls import path
from postings import views

urlpatterns = [
    path('', views.PostingView.as_view(), name='posting_list'),
    path('<str:id>/', views.PostingDetail.as_view(), name='posting_detail'),
]