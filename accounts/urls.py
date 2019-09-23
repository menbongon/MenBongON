from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('test/', views.test, name="test"),
    path('model/',views.generate, name="generate"),
    path('find/', views.find, name="find"),
    path('findid/', views.find_id, name="find_id"),
    path('findpw/', views.find_pw, name="find_pw"),
]