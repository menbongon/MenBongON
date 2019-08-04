from django.shortcuts import render, get_object_or_404, redirect

def mypage(request):
    return render(request, 'mypage.html')
