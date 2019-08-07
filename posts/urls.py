from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('notice/new/', views.notice_new, name="newnotice"),
    path('notice/<int:post_id>/', views.notice_detail, name="notice_detail"),
    
    path('promotion/', views.promotion, name="promotion"),
    path('promotion/new/', views.promotion_new, name="newpromotion"),
    path('promotion/<int:post_id>', views.promotion_detail, name="promotion_detail"),
   
    path('qna/', views.qna, name="qna"),
    path('qna/new/', views.qna_new, name="newqna"),
    path('qna/<int:post_id>', views.qna_detail, name="qna_detail"), 

    path('oneonone/', views.oneonone, name="oneonone"),
    path('oneonone/new/', views.oneonone_new, name="newoneonone"),
    path('oneonone/<int:post_id>/', views.oneonone_detail, name="oneonone_detail"),
    
    path('review/', views.review, name="review"),
]

