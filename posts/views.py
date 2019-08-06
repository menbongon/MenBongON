from django.shortcuts import render, redirect, get_object_or_404
from .models import Promotion_post, Promotion_comment, QandA_post, QandA_comment

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
    return render(request, 'promotionwrite.html') #권한과 상관없이 이동가능하게 하였음. 추후 수정
    #return redirect('promotion')

def promotionCreate(request):
    return render(request, 'promotionboard.html')

def promotionDetail(request, promotion_id):
    details = get_object_or_404(Promotion_post, pk = promotion_id)
    return render(request, 'promotiondetail.html', {'details':details})

def qna(request):
    return render(request, 'qnaboard.html')

def qnaWrite(request):
    user_type=request.user.user_type
    if user_type == 3:
        return render(request, 'qnawrite.html')
    return render(request, 'qnawrite.html') #권한과 상관없이 이동가능하게 하였음. 추후 수정
    #return redirect('qna')

def qnaCreate(request):
    return render(request, 'qnaboard.html')

def qnaDetail(request, qna_id):
    details = get_object_or_404(QandA_post, pk = qna_id)
    return render(request, 'qnadetail.html', {'details':details})

def review(request):
    return render(request, 'reviewboard.html')
