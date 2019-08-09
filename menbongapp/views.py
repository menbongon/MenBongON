from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import University

def intro(request):
    return render(request, 'intro.html')


def home(request):
    username=request.user.username
    password=request.user.password
    return render(request, 'home.html',{'username':username,'password':password})

def menbong(request):
    return render(request, 'menbong.html')

def admission(request):
    university = University.objects.all()
    return render(request, 'univ_admission.html', {'university':university})

def entrance_info(request):
    return render(request, 'entrance_info.html')