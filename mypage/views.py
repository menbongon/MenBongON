from django.shortcuts import render, get_object_or_404, redirect

def mypage(request):
    try:
        username=request.user.username
        password=request.user.password
    except:
        redirect('intro')
    return render(request, 'mypage.html')
