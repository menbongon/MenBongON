from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import University

def intro(request):
    return render(request, 'intro.html')


def home(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    return render(request, 'home.html',{'username':username,'password':password})

def menbong(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    return render(request, 'menbong.html')

def admission(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    university = University.objects.all()
    return render(request, 'univ_admission.html', {'university':university})

def entrance_info(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    return render(request, 'entrance_info.html')


def programmer(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    return render(request, 'programmerintro.html')