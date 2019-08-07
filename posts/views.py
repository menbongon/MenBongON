from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.http import HttpResponse
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

def review(request):
    return render(request, 'reviewboard.html')

def oneonone(request):
    oneonone_posts = Oneonone_post.objects.all()
    return render(request, 'oneononeboard.html', {'oneonone_posts': oneonone_posts})


def oneonone_detail(request, post_id):
    oneonone_detail = get_object_or_404(Oneonone_post, pk = post_id)
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


def oneonone_new(request):
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
