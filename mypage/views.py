from django.shortcuts import render, get_object_or_404, redirect

def mypage(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        return render(request, 'intro.html')
    return render(request, 'mypage.html')
