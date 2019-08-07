from django import forms
from .models import *

class NoticePostForm(forms.ModelForm):
    class Meta:
        model = Notice_post
        fields = ['title', 'body', 'image']
    

class NoticeCommentForm(forms.ModelForm):
    class Meta:
        model = Notice_comment
        fields = ['body']


class OneononePostForm(forms.ModelForm):
    class Meta:
        model = Oneonone_post
        fields = ['title', 'body', 'post_password']

class OneononeCommentForm(forms.ModelForm):
    class Meta:
        model = Oneonone_comment
        fields = ['body']