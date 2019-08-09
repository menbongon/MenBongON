from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  
    name = models.CharField(max_length=500,null=True, blank=True)
    phone_number = models.CharField(max_length=500,null=True, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=500,null=True, blank=True)
    code = models.CharField(max_length=500,null=True, blank=True)

class Senior(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=500,null=True, blank=True)
    major = models.CharField(max_length=500,null=True, blank=True)
    student_number = models.CharField(max_length=500,null=True, blank=True)
    major_type = models.CharField(max_length=500,null=True, blank=True)
    department = models.CharField(max_length=500,null=True, blank=True)
    
class Junior(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=500,null=True, blank=True)
    major = models.CharField(max_length=500,null=True, blank=True)
    student_number = models.CharField(max_length=500,null=True, blank=True)
    major_type = models.CharField(max_length=500,null=True, blank=True)
    department = models.CharField(max_length=500,null=True, blank=True)

class Student(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=500,null=True, blank=True)
    major = models.CharField(max_length=500,null=True, blank=True)
    student_number = models.CharField(max_length=500,null=True, blank=True)
    major_type = models.CharField(max_length=500,null=True, blank=True)
    
class Mentee(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    highschool = models.CharField(max_length=500,null=True, blank=True)
    