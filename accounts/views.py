from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth

User = get_user_model()

# Create your views here.
def first(request):
    return render(request, 'first.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error':'wrong~'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('first')

def home(request):
    username=request.user.username
    password=request.user.password
    return render(request, 'home.html',{'username':username,'password':password})