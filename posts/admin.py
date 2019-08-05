from django.contrib import admin
from .models import Promotion_post, QandA_post, Promotion_comment, QandA_comment

# Register your models here.
admin.site.register(Promotion_post)
admin.site.register(QandA_post)
admin.site.register(Promotion_comment)
admin.site.register(QandA_comment)