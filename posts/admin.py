from django.contrib import admin
from .models import *

# Register your models here.

class NoticePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'pub_date'] 

class NoticeCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

class PromotionPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'pub_date'] 

class PromotionCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

class QnANoticePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'pub_date'] 

class QnACommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

class OneononePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'title', 'post_password', 'pub_date'] 

class OneononeCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_id', 'post', 'post_id', 'body'] 

admin.site.register(Notice_post, NoticePostAdmin)
admin.site.register(Notice_comment, NoticeCommentAdmin)

admin.site.register(Promotion_post, PromotionPostAdmin)
admin.site.register(Promotion_comment, PromotionCommentAdmin)

admin.site.register(QnA_post,QnANoticePostAdmin)
admin.site.register(QnA_comment, QnACommentAdmin)

admin.site.register(Oneonone_post, OneononePostAdmin)
admin.site.register(Oneonone_comment, OneononeCommentAdmin)

admin.site.register(Review1_post)
admin.site.register(Review2_post)

admin.site.register(Review1_post_comment)
admin.site.register(Review2_post_comment)

admin.site.register(Review1_post_image)
admin.site.register(Review2_post_image)
