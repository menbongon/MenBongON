from django import forms
from .models import *

# 공지게시판
class NoticePostForm(forms.ModelForm):
    class Meta:
        model = Notice_post
        fields = ['title', 'body', 'image']
    
    def __init__(self, *args, **kwargs):
        super(NoticePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "본문"
        self.fields['image'].label = "사진"


class NoticeCommentForm(forms.ModelForm):
    class Meta:
        model = Notice_comment
        fields = ['body']
    def __init__(self, *args, **kwargs):
        super(NoticeCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "댓글"


# 홍보게시판
class PromotionPostForm(forms.ModelForm):
    class Meta:
        model = Promotion_post
        fields = ['title', 'body', 'image']
    
    def __init__(self, *args, **kwargs):
        super(PromotionPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "본문"
        self.fields['image'].label = "사진"    

class PromotionCommentForm(forms.ModelForm):
    class Meta:
        model = Promotion_comment
        fields = ['body']
    
    def __init__(self, *args, **kwargs):
        super(PromotionCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "댓글"

# Q&A게시판
class QnAPostForm(forms.ModelForm):
    class Meta:
        model = QnA_post
        fields = ['title', 'body', 'image']

    def __init__(self, *args, **kwargs):
        super(QnAPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "본문"
        self.fields['image'].label = "사진"

class QnACommentForm(forms.ModelForm):
    class Meta:
        model = QnA_comment
        fields = ['body']
    def __init__(self, *args, **kwargs):
        super(QnACommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "댓글"
# 일대일 게시판
class OneononePostForm(forms.ModelForm):
    class Meta:
        model = Oneonone_post
        fields = ['title', 'body', 'post_password']

    def __init__(self, *args, **kwargs):
        super(OneononePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "본문"
        self.fields['post_password'].label = "비밀번호"

class OneononeCommentForm(forms.ModelForm):
    class Meta:
        model = Oneonone_comment
        fields = ['body']
    def __init__(self, *args, **kwargs):
        super(OneononeCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "댓글"
