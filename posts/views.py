from django.shortcuts import render, redirect

def notice(request):
    return render(request, 'noticeboard.html')

def oneonone(request):
    return render(request, 'oneononeboard.html')

def promotion(request):
    return render(request, 'promotionboard.html')

def promotionWrite(request):
    user_type=request.user.user_type
    if user_type == 0 or user_type == 1:
        return render(request, 'promotionwrite.html')
    return redirect('promotion')
    
def qna(request):
    return render(request, 'qnaboard.html')

def qnaWrite(request):
    user_type=request.user.user_type
    if user_type == 3:
        return render(request, 'qnawrite.html')
    return redirect('qna')

def review(request):
    return render(request, 'reviewboard.html')
