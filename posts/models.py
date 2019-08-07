from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# 공지사항 (작성자, 제목, 내용, 이미지, 작성 시간)
# id(integer) author_id(integer) body(text) image(varchar(100)) pub_date(datetime) title(varchar(500)) 
class Notice_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, default='공지')
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return str(self.title)

    def summary(self):
        return self.body[:100]


# 공지사항 댓글 (작성자, 어떤 글, 내용)
# id(integer) author_id(integer) post_id(integer) body(text)
class Notice_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Notice_post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()


#홍보 게시판 (작성자, 제목, 내용, 홍보포스터, 작성시간)
class Promotion_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, default='홍보')
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    #event_date = models.DateTimeField('event day')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

# 홍보게시판 댓글 (작성자, 어떤 글, 내용, 작성시간)
class Promotion_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Notice_post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

#Q&A 게시판 (작성자, 제목, 내용, 사진, 작성시간)
class QnA_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, default='Q&A')
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

# Q&A 게시판 댓글 (작성자, 어떤 글, 작성시간, 내용)
class QnA_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Notice_post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)


# 일대일 (작성자, 제목, 내용, 비밀번호, 작성 시간)
# id(integer) author_id(integer) body(text) post_password(varchar(500)) pub_date(datetime) title(varchar(500)) 
class Oneonone_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, default='일대일상담신청')
    body = models.TextField(null=True, blank=True)
    post_password = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

# 일대일 댓글 (작성자,어떤 글, 내용)
# id(integer) author_id(integer) post_id(integer) body(text)
class Oneonone_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Oneonone_post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()

