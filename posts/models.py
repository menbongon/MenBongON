from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

#홍보 게시판 (작성자, 제목, 작성시간, 내용, 홍보포스터)
class Promotion_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(null=True, upload_to='images/')
    #event_date = models.DateTimeField('event day')
    
    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

#Q&A 게시판 (제목, 작성시간, 내용)
class QandA_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

# 홍보게시판 댓글 (작성자, 어떤 글, 작성시간, 내용)
class Promotion_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Promotion_post, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    comment = models.TextField(max_length=500)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment

# Q&A 게시판 댓글 (작성자, 어떤 글, 작성시간, 내용)
class QandA_comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(QandA_post, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    comment = models.TextField(max_length=500)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment