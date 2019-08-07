from django import forms
from .models import *

# 공지게시판
class NoticePostForm(forms.ModelForm):
    class Meta:
        model = Notice_post
        fields = ['title', 'body', 'image']
    

class NoticeCommentForm(forms.ModelForm):
    class Meta:
        model = Notice_comment
        fields = ['body']

# 홍보게시판
class PromotionPostForm(forms.ModelForm):
    class Meta:
        model = Notice_post
        fields = ['title', 'body', 'image']
    

class PromotionCommentForm(forms.ModelForm):
    class Meta:
        model = Notice_comment
        fields = ['body']

# Q&A게시판
class QnAPostForm(forms.ModelForm):
    class Meta:
        model = Notice_post
        fields = ['title', 'body', 'image']
    

class QnACommentForm(forms.ModelForm):
    class Meta:
        model = Notice_comment
        fields = ['body']

# 일대일 게시판
class OneononePostForm(forms.ModelForm):
    class Meta:
        model = Oneonone_post
        fields = ['title', 'body', 'post_password']

class OneononeCommentForm(forms.ModelForm):
    class Meta:
        model = Oneonone_comment
        fields = ['body']
