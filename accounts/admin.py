from django.contrib import admin
from .models import *
# from django.contrib.auth.models import User
# Register your models here.

admin.site.register(User)

admin.site.register(Senior)
admin.site.register(Junior)
admin.site.register(Student)
admin.site.register(Mentee)
admin.site.register(University)
admin.site.register(Major_type)