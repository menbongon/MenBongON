from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('oneonone/', views.oneonone, name="oneonone"),
    path('promotion/', views.promotion, name="promotion"),
    path('promotion/write/', views.promotion, name="promotionwrite"),
    path('qna/', views.qna, name="qna"),
    path('qna/write/', views.qna, name="qnawrite"),
    path('review/', views.review, name="review"),
]