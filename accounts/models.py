from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  
    name = models.CharField(max_length=100,null=True, blank=True)
    phone_number = models.CharField(max_length=4,null=True, blank=True)
    phone_number2 = models.CharField(max_length=4,null=True, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=100,null=True, blank=True)
    code = models.CharField(max_length=100,null=True, blank=True)
    nickname = models.CharField(max_length=100,null=True, blank=True)

class Senior(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=100,null=True, blank=True)
    major = models.CharField(max_length=100,null=True, blank=True)
    student_number = models.CharField(max_length=100,null=True, blank=True)
    major_type = models.CharField(max_length=100,null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    menbong = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user_id)

class Junior(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=100,null=True, blank=True)
    major = models.CharField(max_length=100,null=True, blank=True)
    student_number = models.CharField(max_length=100,null=True, blank=True)
    major_type = models.CharField(max_length=100,null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    menbong = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user_id)

class Student(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=100,null=True, blank=True)
    major = models.CharField(max_length=100,null=True, blank=True)
    student_number = models.CharField(max_length=100,null=True, blank=True)
    major_type = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
       return str(self.user_id)   

class Mentee(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    highschool = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return str(self.user_id)
    
class University(models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)
    admission_link = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name
        