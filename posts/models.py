from django.db import models
from django.utils import timezone

#게시판
class Promotion_post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    event_date = models.DateTimeField('event day')
    body = models.TextField()
    
    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class QandA_post(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#댓글
class Promotion_comment(models.Model):
    #writer = models.user.username
    pub_date = models.DateTimeField('date published')
    comment = models.TextField(max_length=500)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment

class QandA_comment(models.Model):
    #writer = models.user.username
    pub_date = models.DateTimeField('date published')
    comment = models.TextField(max_length=500)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment