from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Promotion_post, Promotion_comment, QandA_post, QandA_comment
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def notice(request):
    return render(request, 'noticeboard.html')

def oneonone(request):
    return render(request, 'oneononeboard.html')

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
    return render(request, 'qnaboard.html',{'qnas:'})

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
