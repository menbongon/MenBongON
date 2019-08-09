from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.http import HttpResponse
import os
import logging

import os

def notice(request):
    notice_posts = Notice_post.objects.all()
    # notice_list = Notice_post.objects.all()
    # paginator = Paginator(notice_list, 10)
    # page
    return render(request, 'noticeboard.html', {'notice_posts': notice_posts})

def notice_detail(request, post_id):
    notice_detail = get_object_or_404(Notice_post, pk = post_id)
    if request.method == 'POST':
        form = NoticeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = notice_detail
            comment.save()

            newform = NoticeCommentForm()
            notice_detail = get_object_or_404(Notice_post, pk = post_id)
            notice_comments = Notice_comment.objects.filter(
                post_id = post_id
            )
            return render(request, 'noticepost.html', {'notice': notice_detail, 'notice_comments': notice_comments, 'form': newform})
        else:
            return redirect('home')
    else:
        newform = NoticeCommentForm()
        notice_detail = get_object_or_404(Notice_post, pk = post_id)
        notice_comments = Notice_comment.objects.filter(
            post_id = post_id
        )
        return render(request, 'noticepost.html', {'notice': notice_detail, 'notice_comments': notice_comments, 'form': newform})


def notice_new(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.user.user_type == 0:
        if request.method == 'POST':
            form = NoticePostForm(request.POST, request.FILES) 
            if form.is_valid():
                # is_valid는 입력값 없을 시 등 예외시 오류 띄워줌.
                # 저장하지 않고 모델 객체 반환
                post = form.save(commit=False)
                post.author = request.user
                post.pub_date = timezone.now()
                post.save()
                return redirect('notice_detail', post_id=post.id)
            else:
                return redirect('notice')

        # 2. 빈 페이지를 띄워주는 기능 -> GET
        else:
            form = NoticePostForm()
            return render(request, 'newnotice.html', {'form': form})
    else:
        return render(request, 'warning.html')

def notice_remove(request, post_id):
    notice = get_object_or_404(Notice_post, pk = post_id)
    if request.user.user_type == 0 or request.user.id == oneonone_post.author_id:
        notice.delete()
        return redirect('notice')
    else:
        return render(request, 'warning.html')

def notice_edit(request, post_id):
    notice = get_object_or_404(Notice_post, pk = post_id)
    if request.user.id == notice.author_id:
        if request.method == 'POST':
            form = NoticePostForm(request.POST, request.FILES)
            if form.is_valid():
                notice.title = form.cleaned_data['title']
                notice.body = form.cleaned_data['body']
                notice.image = form.cleaned_data['image']
                notice.save()
                return redirect('notice_detail', post_id=notice.id)
        else:
            form = NoticePostForm(instance=notice)
            return render(request, 'editnotice.html', {'form': form})
    else:
        return render(request, 'warning.html')

def promotion(request):
    promotion_posts = Promotion_post.objects.all()
    return render(request, 'promotionboard.html', {'promotion_posts': promotion_posts})

def promotion_detail(request, post_id):
    promotion_detail = get_object_or_404(Promotion_post, pk = post_id)
    if request.method == 'POST':
        form = PromotionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = promotion_detail
            comment.save()

            newform = PromotionCommentForm()
            promotion_detail = get_object_or_404(Promotion_post, pk = post_id)
            promotion_comments = Promotion_comment.objects.filter(
                post_id = post_id
            )
            return render(request, 'promotionpost.html', {'promotion': promotion_detail, 'promotion_comments': promotion_comments, 'form': newform})
        else:
            return redirect('home')
    else:
        newform = PromotionCommentForm()
        promotion_detail = get_object_or_404(Promotion_post, pk = post_id)
        promotion_comments = Promotion_comment.objects.filter(
            post_id = post_id
        )
        return render(request, 'promotionpost.html', {'promotion':  promotion_detail, 'promotion_comments': promotion_comments, 'form': newform})


def promotion_new(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = PromotionPostForm(request.POST, request.FILES) 
        if form.is_valid():
            # is_valid는 입력값 없을 시 등 예외시 오류 띄워줌.
            # 저장하지 않고 모델 객체 반환
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('promotion_detail', post_id=post.id)
        else:
            return redirect('promotion')

    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = PromotionPostForm()
        return render(request, 'newpromotion.html', {'form': form})

def promotion_remove(request, post_id):
    promotion_detail = get_object_or_404(Promotion_post, pk = post_id)
    if request.user.user_type == 0 or request.user.id == promotion_detail.author_id:
        promotion_detail.delete()
        return redirect('promotion')
    else:
        return render(request, 'warning.html')

def promotion_edit(request, post_id):
    promotion_detail = get_object_or_404(Promotion_post, pk = post_id)
    if request.user.id == promotion_detail.author_id:
        if request.method == 'POST':
            form = PromotionPostForm(request.POST, request.FILES)
            if form.is_valid():
                promotion_detail.title = form.cleaned_data['title']
                promotion_detail.body = form.cleaned_data['body']
                promotion_detail.image = form.cleaned_data['image']
                promotion_detail.save()
                return redirect('promotion_detail', post_id=promotion_detail.id)
        else:
            form = PromotionPostForm(instance=promotion_detail)
            return render(request, 'editpromotion.html', {'form': form})
    else:
        return render(request, 'warning.html')

def qna(request):
    qna_posts = QnA_post.objects.all()
    return render(request, 'qnaboard.html', {'qna_posts': qna_posts})

def qna_detail(request, post_id):
    qna_detail = get_object_or_404(QnA_post, pk = post_id)
    if request.method == 'POST':
        form = QnACommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = qna_detail
            comment.save()

            newform = QnACommentForm()
            qna_detail = get_object_or_404(QnA_post, pk = post_id)
            qna_comments = QnA_comment.objects.filter(
                post_id = post_id
            )
            return render(request, 'qnapost.html', {'qna': qna_detail, 'qna_comments': qna_comments, 'form': newform})
        else:
            return redirect('home')
    else:
        newform = QnACommentForm()
        qna_detail = get_object_or_404(QnA_post, pk = post_id)
        qna_comments = QnA_comment.objects.filter(
            post_id = post_id
        )
        return render(request, 'qnapost.html', {'qna': qna_detail, 'qna_comments': qna_comments, 'form': newform})


def qna_new(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = QnAPostForm(request.POST, request.FILES) 
        if form.is_valid():
            # is_valid는 입력값 없을 시 등 예외시 오류 띄워줌.
            # 저장하지 않고 모델 객체 반환
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('qna_detail', post_id=post.id)
        else:
            return redirect('qna')

    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = QnAPostForm()
        return render(request, 'newqna.html', {'form': form})

def qna_remove(request, post_id):
    qna_detail = get_object_or_404(QnA_post, pk = post_id)
    if request.user.user_type == 0 or request.user.id == qna_detail.author_id:
        qna_detail.delete()
        return redirect('qna')
    else:
        return render(request, 'warning.html')

def qna_edit(request, post_id):
    qna_detail = get_object_or_404(QnA_post, pk = post_id)
    if request.user.id == qna_detail.author_id:
        if request.method == 'POST':
            form = QnAPostForm(request.POST, request.FILES)
            if form.is_valid():
                qna_detail.title = form.cleaned_data['title']
                qna_detail.body = form.cleaned_data['body']
                qna_detail.image = form.cleaned_data['image']
                qna_detail.save()
                return redirect('qna_detail', post_id=qna_detail.id)
        else:
            form = QnAPostForm(instance=qna_detail)
            return render(request, 'editqna.html', {'form': form})
    else:
        return render(request, 'warning.html')



def review(request):
    return render(request, 'reviewboard.html')

def oneonone(request):
    oneonone_posts = Oneonone_post.objects.all()
    return render(request, 'oneononeboard.html', {'oneonone_posts': oneonone_posts})


def oneonone_detail(request, post_id):
    oneonone_detail = get_object_or_404(Oneonone_post, pk = post_id)
    if request.user.user_type == 0 or request.user.user_type == 1 or request.user.id == oneonone_detail.author_id:
        if request.method == 'POST':
            form = OneononeCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = oneonone_detail
                comment.save()

                newform = OneononeCommentForm()
                oneonone_detail = get_object_or_404(Oneonone_post, pk = post_id)
                oneonone_comments = Oneonone_comment.objects.filter(
                    post_id = post_id
                )
                return render(request, 'oneononepost.html', {'oneonone': oneonone_detail, 'oneonone_comments': oneonone_comments, 'form': newform})
            else:
                return redirect('home')
        else:
            newform = OneononeCommentForm()
            oneonone_detail = get_object_or_404(Oneonone_post, pk = post_id)
            oneonone_comments = Oneonone_comment.objects.filter(
                post_id = post_id
            )
            return render(request, 'oneononepost.html', {'oneonone': oneonone_detail, 'oneonone_comments': oneonone_comments, 'form': newform})
    else:
        return render(request, 'warning.html')


def oneonone_new(request):
    if request.user.user_type == 0 or request.user.user_type == 1 or request.user.user_type == 3:
        # 1. 입력된 내용을 처리하는 기능 -> POST
        if request.method == 'POST':
            form = OneononePostForm(request.POST) 
            if form.is_valid():
                # is_valid는 입력값 없을 시 등 예외시 오류 띄워줌.
                # 저장하지 않고 모델 객체 반환
                post = form.save(commit=False)
                post.author = request.user
                post.pub_date = timezone.now()
                post.save()
                return redirect('oneonone_detail', post_id=post.id)
            else:
                return redirect('oneonone')

        # 2. 빈 페이지를 띄워주는 기능 -> GET
        else:
            form = OneononePostForm()
            return render(request, 'newoneonone.html', {'form': form})
    else:
        return render(request, 'warning.html')


def oneonone_remove(request, post_id):
    oneonone_post = get_object_or_404(Oneonone_post, pk = post_id)
    if request.user.user_type == 0 or request.user.id == oneonone_post.author_id:
        oneonone_post.delete()
        return redirect('oneonone')
    else:
        return render(request, 'warning.html')

def oneonone_edit(request, post_id):
    oneonone_post = get_object_or_404(Oneonone_post, pk = post_id)
    if request.user.id == oneonone_post.author_id:
        if request.method == 'POST':
            form = OneononePostForm(request.POST)
            if form.is_valid():
                oneonone_post.title = form.cleaned_data['title']
                oneonone_post.body = form.cleaned_data['body']
                oneonone_post.post_password = form.cleaned_data['post_password']
                oneonone_post.save()
                return redirect('oneonone_detail', post_id=oneonone_post.id)
        else:
            form = OneononePostForm(instance=oneonone_post)
            return render(request, 'editoneonone.html', {'form': form})
    else:
        return render(request, 'warning.html')

def review1_board(request):
    if request.method == "GET":
        review1_posts = Review1_post.objects.all()
        try:
            if request.GET["university"] != "":
                review1_posts = review1_posts.filter(university=request.GET["university"])
            if request.GET["major"] != "":
                review1_posts = review1_posts.filter(major=request.GET["major"])
            if request.GET["major_type"] != "":
                review1_posts = review1_posts.filter(major_type=request.GET["major_type"])
            if request.GET["region"] != "":
                review1_posts = review1_posts.filter(region=request.GET["region"])
        except:
            pass
        # review1_posts = 0
        return render(request, 'review1_board.html',{'review1_posts' : review1_posts})

def review1_post_detail(request,pk):
    if request.method =="GET":
        review1_post = Review1_post.objects.get(id=pk)
        review1_post_comments = Review1_post_comment.objects.filter(commented_post=pk)
        review1_post_images = Review1_post_image.objects.filter(imaged_post=pk)
        print(review1_post_images)
        return render(request, 'review1_post_detail.html',{'review1_post' : review1_post, 'review1_post_comments' : review1_post_comments, 'review1_post_images' : review1_post_images})
        
    else:
        new_review1_post_comment = Review1_post_comment()
        new_review1_post_comment.user = request.user.username
        new_review1_post_comment.content = request.POST["content"]
        new_review1_post_comment.commented_post = pk
        new_review1_post_comment.save()

        review1_post = Review1_post.objects.get(id=pk)
        review1_post_comments = Review1_post_comment.objects.filter(commented_post=pk)
        review1_post_images = Review1_post_image.objects.filter(imaged_post=pk)
        
        return render(request, 'review1_post_detail.html',{'review1_post' : review1_post, 'review1_post_comments' : review1_post_comments, 'review1_post_images' : review1_post_images})

def review1_post_create(request):
    if request.method == "GET":
        return render(request, 'review1_post_create.html')
    else:
        if request.user.user_type == 0 or request.user.user_type == 1:
        # if request.user.user_type != 100:
            new_review1_post = Review1_post()
            new_review1_post.title = request.POST['title']
            new_review1_post.user =  request.user.username
            new_review1_post.content = request.POST['content']
            new_review1_post.university = request.POST['university']
            new_review1_post.major = request.POST['major']
            new_review1_post.major_type = request.POST['major_type']
            new_review1_post.region = request.POST['region']
            # a=request.POST['picture']
            # a=request.POST
            # a=request.POST['csrfmiddlewaretoken']
            # a=request.POST.get('picture', '')
            # a=type(request.FILES)
            # new_post.image = request.FILES

            # a="asd"
            new_review1_post.save()

            a = request.FILES['picture']
            new_review1_post.image_url = "/media/review1/post/image"+str(new_review1_post.id)+"/"+a.name
            
            for a in request.FILES.getlist('picture'):
                # a=request.FILES['picture']
                # new_review1_post.image_url = "/media/review1/post/image"+str(new_review1_post.id)+"/"+a.name
                new_review1_post_image = Review1_post_image()
                new_review1_post_image.imaged_post = new_review1_post.id
                new_review1_post_image.image_url = "/media/review1/post/image"+str(new_review1_post.id)+"/"+a.name
                new_review1_post_image.save()

                fs=FileSystemStorage()
                fn=fs.save("review1/post/image"+str(new_review1_post.id)+"/"+a.name,a)

            # a=fs.url(fn)
            # new_post.image_url = a

            new_review1_post.save()

            review1_posts = Review1_post.objects.all()
    # return render(request, 'post_list.html',{'posts' : posts})
            return redirect('review1_board')
        else:
            return redirect('review1_board')


def review2_board(request):
    if request.method == "GET":
        review2_posts = Review2_post.objects.all()
        try:
            if request.GET["university"] != "":
                review2_posts = review2_posts.filter(university=request.GET["university"])
            if request.GET["major"] != "":
                review2_posts = review2_posts.filter(major=request.GET["major"])
            if request.GET["major_type"] != "":
                review2_posts = review2_posts.filter(major_type=request.GET["major_type"])
            if request.GET["region"] != "":
                review2_posts = review2_posts.filter(region=request.GET["region"])
        except:
            pass
        # review2_posts = 0
        return render(request, 'review2_board.html',{'review2_posts' : review2_posts})

def review2_post_detail(request,pk):
    if request.method == "GET":
        review2_post = Review2_post.objects.get(id=pk)
        review2_post_comments = Review2_post_comment.objects.filter(commented_post=pk)
        review2_post_images = Review2_post_image.objects.filter(imaged_post=pk)
        print(review2_post_images)
        return render(request, 'review2_post_detail.html',{'review2_post' : review2_post, 'review2_post_comments' : review2_post_comments, 'review2_post_images' : review2_post_images})
        
    else:
        new_review2_post_comment = Review2_post_comment()
        new_review2_post_comment.user = request.user.username
        new_review2_post_comment.content = request.POST["content"]
        new_review2_post_comment.commented_post = pk
        new_review2_post_comment.save()

        review2_post = Review2_post.objects.get(id=pk)
        review2_post_comments = Review2_post_comment.objects.filter(commented_post=pk)
        review1_post_images = Review1_post_image.objects.filter(imaged_post=pk)
        
        return render(request, 'review2_post_detail.html',{'review2_post' : review2_post, 'review2_post_comments' : review2_post_comments, 'review2_post_images' : review2_post_images})
        
def review2_post_create(request):
    if request.method == "GET":
        return render(request, 'review2_post_create.html')
    else:
        if request.user.user_type == 0 or request.user.user_type == 1:
        # if request.user.user_type != 100:
            new_review2_post = Review2_post()
            new_review2_post.title = request.POST['title']
            new_review2_post.user =  request.user.username
            new_review2_post.content = request.POST['content']
            new_review2_post.university = request.POST['university']
            new_review2_post.major = request.POST['major']
            new_review2_post.major_type = request.POST['major_type']
            new_review2_post.region = request.POST['region']
            # a=request.POST['picture']
            # a=request.POST
            # a=request.POST['csrfmiddlewaretoken']
            # a=request.POST.get('picture', '')
            # a=type(request.FILES)
            # new_post.image = request.FILES

            # a="asd"
            new_review2_post.save()

            a = request.FILES['picture']
            new_review2_post.image_url = "/media/review2/post/image"+str(new_review2_post.id)+"/"+a.name
            
            for a in request.FILES.getlist('picture'):
                # a=request.FILES['picture']
                # new_review2_post.image_url = "/media/review2/post/image"+str(new_review2_post.id)+"/"+a.name
                new_review2_post_image = Review2_post_image()
                new_review2_post_image.imaged_post = new_review2_post.id
                new_review2_post_image.image_url = "/media/review2/post/image"+str(new_review2_post.id)+"/"+a.name
                new_review2_post_image.save()

                fs=FileSystemStorage()
                fn=fs.save("review2/post/image"+str(new_review2_post.id)+"/"+a.name,a)

            # a=fs.url(fn)
            # new_post.image_url = a
        
            new_review2_post.save()

            review2_posts = Review2_post.objects.all()
    # return render(request, 'post_list.html',{'posts' : posts})
            return redirect('review2_board')
        else:
            return redirect('review2_board')
