from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('oneonone/', views.oneonone, name="oneonone"),
    path('promotion/', views.promotion, name="promotion"),
    path('qna/', views.qna, name="qna"),
    path('review1/board/<page>', views.review1_board, name="review1_board"),
    path('review1/post/create', views.review1_post_create, name="review1_post_create"),
    path('review1/post/detail/<pk>', views.review1_post_detail, name="review1_post_detail"),
    path('review2/board/<page>', views.review2_board, name="review2_board"),
    path('review2/post/create', views.review2_post_create, name="review2_post_create"),
    path('review2/post/detail/<pk>', views.review2_post_detail, name="review2_post_detail"),

]