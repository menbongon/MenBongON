from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.http import HttpResponse

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



def promotion(request):
    return render(request, 'promotionboard.html')

def qna(request):
    return render(request, 'qnaboard.html')

def review(request):
    return render(request, 'reviewboard.html')
