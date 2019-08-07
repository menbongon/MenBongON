from django.contrib import admin
from .models import Promotion_post, QandA_post, Promotion_comment, QandA_comment
from .models import *

class NoticePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'pub_date'] 

class NoticeCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

class OneononePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'post_password', 'pub_date'] 

class OneononeCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

admin.site.register(Notice_post, NoticePostAdmin)
admin.site.register(Notice_comment, NoticeCommentAdmin)
admin.site.register(Oneonone_post, OneononePostAdmin)
admin.site.register(Oneonone_comment, OneononeCommentAdmin)
admin.site.register(Promotion_post)
admin.site.register(QandA_post)
admin.site.register(Promotion_comment)
admin.site.register(QandA_comment)
