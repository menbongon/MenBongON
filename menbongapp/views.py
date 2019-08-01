from django.shortcuts import render, get_object_or_404, redirect

def intro(request):
    return render(request, 'intro.html')

def home(request):
    return render(request, 'home.html')

