from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *
from django.contrib import auth
import logging
from .models import *

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_check"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            except:
                return render(request, 'signup.html', {'error_msg':"아이디가 중복됩니다."})

            user.name = request.POST["name"]
            user.email = request.POST["email"]
            user.phone_number = request.POST["phone_number"]
            user.region = request.POST["region"]
            user.user_type = request.POST["user_type"]
            user.save()
            if user.user_type == "0":
                senior = Senior()
                senior.user_id=user.id
                senior.university = request.POST["university"]
                senior.major = request.POST["major"]
                senior.student_number = request.POST["student_number"]
                senior.major_type = request.POST["major_type"]
                senior.department = request.POST["department"]
                senior.save()
            if user.user_type == "1":
                print("QWE")
                junior = Junior()
                junior.user_id=user.id
                junior.university = request.POST["university"]
                junior.major = request.POST["major"]
                junior.student_number = request.POST["student_number"]
                junior.major_type = request.POST["major_type"]
                junior.department = request.POST["department"]
                junior.save()
            if user.user_type == "2":
                student = Student()
                student.user_id=user.id
                student.university = request.POST["university"]
                student.major = request.POST["major"]
                student.student_number = request.POST["student_number"]
                student.major_type = request.POST["major_type"]
                student.save()
            if user.user_type == "3":
                mentee = Mentee()
                mentee.user_id=user.id
                mentee.highschool = request.POST["highschool"]
                mentee.save()



            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error_msg':"비밀번호와 확인이 다릅니다."})
         
    university = University.objects.all()
    return render(request, 'signup.html', {'university':university})

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'intro.html',{'error':'wrong~'})
    else:
        return render(request, 'intro.html')

def logout(request):
    auth.logout(request)
    return redirect('intro')

def test(request):
    logging.error(request.user.username)
    return redirect('home')
