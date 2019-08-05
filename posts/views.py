from django.shortcuts import render, redirect

def notice(request):
    return render(request, 'noticeboard.html')

def oneonone(request):
    return render(request, 'oneononeboard.html')

def promotion(request):
    return render(request, 'promotionboard.html')

def promotionWrite(request):
    return render(request, 'promotionwrite.html')

def qna(request):
    return render(request, 'qnaboard.html')

def qnaWrite(request):
    return render(request, 'qnawrite.html')

def review(request):
    return render(request, 'reviewboard.html')
