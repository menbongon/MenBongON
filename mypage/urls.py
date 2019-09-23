from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myhome, name="myhome"),
    path('editprofile/', views.mypage, name = "mypage"),
]