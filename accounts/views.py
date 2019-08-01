from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        return redirect('home')

    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        return redirect('intro')

    return redirect('intro')
