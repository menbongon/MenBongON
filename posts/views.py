from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Promotion_post, Promotion_comment, QandA_post, QandA_comment
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
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


def promotion(request):
    promotions = Promotion_post.objects
    return render(request, 'promotionboard.html', {'promotions':promotions})

def promotionWrite(request):
    user_type=request.user.user_type
    if user_type == 0 or user_type == 1:
        return render(request, 'promotionwrite.html')
    return render(request, 'promotionwrite.html') #권한과 상관없이 이동가능하게 하였음. 추후 수정
    #return redirect('promotion')

def promotionCreate(request):
    promotion = Promotion_post()
    if request.method == "POST":
        promotion.title = request.POST['title']
        promotion.body = request.POST['body']
        promotion.pub_date = timezone.datetime.now()
        promotion.save() # 쿼리셋 메소드 (데이터베이스에 저장)
        
        prom_img=request.FILES['picture']
        os.makedirs(("static/userimage/promotion"+str(promotion.id)))
        promotion.image = "userimage/promotion"+str(promotion.id)+"/"+prom_img.name
        fs=FileSystemStorage()
        fn=fs.save("promotion"+str(promotion.id)+"/"+prom_img.name,prom_img)
        promotion.save()

        return redirect('../'+str(promotion.id))
    return render(request, 'promotionboard.html')

def promotionDetail(request, promotion_id):
    details = get_object_or_404(Promotion_post, pk = promotion_id)
    return render(request, 'promotiondetail.html', {'details':details})

def promotionComment(request, promotion_id):
    details = get_object_or_404(Promotion_post, pk = promotion_id)
    #if request.method == 'POST':
    return render(request, 'promotiondetail.html', {'details':details})

def qna(request):
    qnas = QandA_post.objects
    return render(request, 'qnaboard.html',{'qnas':qnas})

def qnaWrite(request):
    user_type=request.user.user_type
    if user_type == 3:
        return render(request, 'qnawrite.html')
    return render(request, 'qnawrite.html') #권한과 상관없이 이동가능하게 하였음. 추후 수정
    #return redirect('qna')

def qnaCreate(request):
    qna = QandA_post()
    if request.method == "POST":
        qna.title = request.POST['title']
        qna.body = request.POST['body']
        qna.pub_date = timezone.datetime.now()
        qna.save() # 쿼리셋 메소드 (데이터베이스에 저장)
        return redirect('../'+str(qna.id))
    return render(request, 'qnaboard.html')

def qnaDetail(request, qna_id):
    details = get_object_or_404(QandA_post, pk = qna_id)
    return render(request, 'qnadetail.html', {'details':details})

# def qnaComment(request, qna_id):
#     details = get_object_or_404(QandA_post, pk = qna_id)
#     return render(request, 'qnadetail.html', {'details':details})

def review(request):
    return render(request, 'reviewboard.html')
