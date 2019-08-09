from django.shortcuts import render, redirect

from posts.models import Review1_post, Review2_post, Review1_post_comment, Review2_post_comment, Review1_post_image, Review2_post_image

from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os

def notice(request):
    return render(request, 'noticeboard.html')

def oneonone(request):
    return render(request, 'oneononeboard.html')

def promotion(request):
    return render(request, 'promotionboard.html')

def qna(request):
    return render(request, 'qnaboard.html')


def review1_board(request, page):
    if request.method == "GET":
        review1_posts = Review1_post.objects.all()
        if request.GET["university"] != "":
            review1_posts = review1_posts.filter(university=request.GET["university"])
        if request.GET["major"] != "":
            review1_posts = review1_posts.filter(major=request.GET["major"])
        if request.GET["major_type"] != "":
            review1_posts = review1_posts.filter(major_type=request.GET["major_type"])
        if request.GET["region"] != "":
            review1_posts = review1_posts.filter(region=request.GET["region"])

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
        
        return render(request, 'review1_post_detail.html',{'review1_post' : review1_post, 'review1_post_comments' : review1_post_comments, 'review1_post_images' : review1_post_images})
        
def review1_post_create(request):
    if request.method == "GET":
        return render(request, 'review1_post_create.html')
    else:
        # if request.user.user_type == 0 or request.user.user_type == 1:
        if request.user.user_type != 100:
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
            new_review1_post.image_url = "mediaimage/review1/post/image"+str(new_review1_post.id)+"/"+a.name
            
            for a in request.FILES.getlist('picture'):
                # a=request.FILES['picture']
                # new_review1_post.image_url = "mediaimage/review1/post/image"+str(new_review1_post.id)+"/"+a.name
                new_review1_post_image = Review1_post_image()
                new_review1_post_image.imaged_post = new_review1_post.id
                new_review1_post_image.image_url = "mediaimage/review1/post/image"+str(new_review1_post.id)+"/"+a.name
                new_review1_post_image.save()

                fs=FileSystemStorage()
                fn=fs.save("review1/post/image"+str(new_review1_post.id)+"/"+a.name,a)

            # a=fs.url(fn)
            # new_post.image_url = a

            new_review1_post.save()

            review1_posts = Review1_post.objects.all()
    # return render(request, 'post_list.html',{'posts' : posts})
            return redirect('review1_board', page=1)
        else:
            return redirect('review1_board', page=1)


def review2_board(request, page):
    if request.method == "GET":
        review2_posts = Review2_post.objects.all()
        if request.GET["university"] != "":
            review2_posts = review2_posts.filter(university=request.GET["university"])
        if request.GET["major"] != "":
            review2_posts = review2_posts.filter(major=request.GET["major"])
        if request.GET["major_type"] != "":
            review2_posts = review2_posts.filter(major_type=request.GET["major_type"])
        if request.GET["region"] != "":
            review2_posts = review2_posts.filter(region=request.GET["region"])

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
        
        return render(request, 'review2_post_detail.html',{'review2_post' : review2_post, 'review2_post_comments' : review2_post_comments, 'review2_post_images' : review2_post_images})
        
def review2_post_create(request):
    if request.method == "GET":
        return render(request, 'review2_post_create.html')
    else:
        # if request.user.user_type == 0 or request.user.user_type == 1:
        if request.user.user_type != 100:
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
            new_review2_post.image_url = "mediaimage/review2/post/image"+str(new_review2_post.id)+"/"+a.name
            
            for a in request.FILES.getlist('picture'):
                # a=request.FILES['picture']
                # new_review2_post.image_url = "mediaimage/review2/post/image"+str(new_review2_post.id)+"/"+a.name
                new_review2_post_image = Review2_post_image()
                new_review2_post_image.imaged_post = new_review2_post.id
                new_review2_post_image.image_url = "mediaimage/review2/post/image"+str(new_review2_post.id)+"/"+a.name
                new_review2_post_image.save()

                fs=FileSystemStorage()
                fn=fs.save("review2/post/image"+str(new_review2_post.id)+"/"+a.name,a)

            # a=fs.url(fn)
            # new_post.image_url = a
        
            new_review2_post.save()

            review2_posts = Review2_post.objects.all()
    # return render(request, 'post_list.html',{'posts' : posts})
            return redirect('review2_board', page=1)
        else:
            return redirect('review2_board', page=1)

