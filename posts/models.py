from django.db import models

# Create your models here.

class Review1_post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    major_type = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    heart_count = models.IntegerField(default=0, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField('imageurl',max_length=1000,default="", null=True, blank=True)

class Review1_post_comment(models.Model):
    commented_post = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    commented_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)

class Review1_post_image(models.Model):
    imaged_post = models.IntegerField(null=True, blank=True)
    image_url = models.URLField('imageurl',max_length=1000,default="", null=True, blank=True)

class Review2_post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    major_type = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    heart_count = models.IntegerField(default=0, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField('imageurl',max_length=1000,default="", null=True, blank=True)

class Review2_post_comment(models.Model):
    commented_post = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    commented_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)

class Review2_post_image(models.Model):
    imaged_post = models.IntegerField(null=True, blank=True)
    image_url = models.URLField('imageurl',max_length=1000,default="", null=True, blank=True)
