from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('notice/new/', views.notice_new, name="newnotice"),
    path('notice/<int:post_id>/', views.notice_detail, name="notice_detail"),

    path('oneonone/', views.oneonone, name="oneonone"),
    path('oneonone/new/', views.oneonone_new, name="newoneonone"),
    path('oneonone/<int:post_id>/', views.oneonone_detail, name="oneonone_detail"),
    
    path('promotion/', views.promotion, name="promotion"),
    path('qna/', views.qna, name="qna"),
    path('review/', views.review, name="review"),
]

