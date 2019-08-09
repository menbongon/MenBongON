from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('notice/new/', views.notice_new, name="newnotice"),
    path('notice/<int:post_id>/', views.notice_detail, name="notice_detail"),
    path('notice/<int:post_id>/remove/', views.notice_remove, name="notice_remove"),
    path('notice/<int:post_id>/edit/', views.notice_edit, name="notice_edit"),
  
    path('promotion/', views.promotion, name="promotion"),
    path('promotion/new/', views.promotion_new, name="newpromotion"),
    path('promotion/<int:post_id>', views.promotion_detail, name="promotion_detail"),
   
    path('qna/', views.qna, name="qna"),

    path('qna/new/', views.qna_new, name="newqna"),
    path('qna/<int:post_id>', views.qna_detail, name="qna_detail"), 

    path('oneonone/', views.oneonone, name="oneonone"),
    path('oneonone/new/', views.oneonone_new, name="newoneonone"),
    path('oneonone/<int:post_id>/', views.oneonone_detail, name="oneonone_detail"),
    path('oneonone/<int:post_id>/remove/', views.oneonone_remove, name="oneonone_remove"),
    path('oneonone/<int:post_id>/edit/', views.oneonone_edit, name="oneonone_edit"),

    path('review1/board', views.review1_board, name="review1_board"),
    path('review1/post/create', views.review1_post_create, name="review1_post_create"),
    path('review1/post/detail/<pk>', views.review1_post_detail, name="review1_post_detail"),
    path('review2/board', views.review2_board, name="review2_board"),
    path('review2/post/create', views.review2_post_create, name="review2_post_create"),
    path('review2/post/detail/<pk>', views.review2_post_detail, name="review2_post_detail"),

]

