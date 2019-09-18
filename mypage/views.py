from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *
from django.contrib import auth
import logging
from .models import *
from posts.models import *

User = get_user_model()

def mypage(request):
    if request.method == 'POST':
        if request.POST["password"] == request.POST["password_check"]:
            user = User.objects.get(id = request.user.id)
            
            user.name = request.POST["name"]
            user.email = request.POST["email"]
            user.phone_number = request.POST["phone_number"]
            user.region = request.POST["region"]
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

        return redirect('home')
    else:  
        # university = University.objects.all()

        my_notice_posts = Notice_post.objects.all().order_by('-pub_date').filter(author_id=request.user.id)
        my_oneonone_posts = Oneonone_post.objects.all().order_by('-pub_date').filter(author_id=request.user.id)
        my_promotion_posts = Promotion_post.objects.all().order_by('-pub_date').filter(author_id=request.user.id)
        my_qna_posts = QnA_post.objects.all().order_by('-pub_date').filter(author_id=request.user.id)
        my_review1_posts = Review1_post.objects.all().order_by('-posted_date').filter(user=request.user.id)
        my_review2_posts = Review2_post.objects.all().order_by('-posted_date').filter(user=request.user.id)

        userType = request.user.user_type
        return render(request, 'mypage.html', {'userType': userType, 'my_notice_posts':my_notice_posts, 'my_oneonone_posts':my_oneonone_posts, 'my_promotion_posts':my_promotion_posts, 'my_qna_posts':my_qna_posts, 'my_review1_posts':my_review1_posts,'my_review2_posts':my_review2_posts})


