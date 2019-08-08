from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('notice/new/', views.notice_new, name="newnotice"),
    path('notice/<int:post_id>/', views.notice_detail, name="notice_detail"),
    path('notice/<int:post_id>/remove/', views.notice_remove, name="notice_remove"),
    path('notice/<int:post_id>/edit/', views.notice_edit, name="notice_edit"),

    path('oneonone/', views.oneonone, name="oneonone"),
    path('oneonone/new/', views.oneonone_new, name="newoneonone"),
    path('oneonone/<int:post_id>/', views.oneonone_detail, name="oneonone_detail"),
    path('oneonone/<int:post_id>/remove/', views.oneonone_remove, name="oneonone_remove"),
    path('oneonone/<int:post_id>/edit/', views.oneonone_edit, name="oneonone_edit"),

    path('promotion/', views.promotion, name="promotion"),
    path('promotion/write/', views.promotionWrite, name="promotionwrite"),
    path('promotion/write/create', views.promotionCreate, name="promotioncreate"),
    path('promotion/<int:promotion_id>', views.promotionDetail, name="promotiondetail"),
    #path('promotion/<int:promotion_id>/comment', views.promotionComment, name="promotioncomment"), 
    path('qna/', views.qna, name="qna"),
    path('qna/write/', views.qnaWrite, name="qnawrite"),
    path('qna/write/create', views.qnaCreate, name="qnacreate"),
    path('qna/<int:qna_id>', views.qnaDetail, name="qnadetail"), 
    #path('qna/<int:qna_id>/comment', views.qnaComment, name="qnacomment"), 
    path('review/', views.review, name="review"),
]

