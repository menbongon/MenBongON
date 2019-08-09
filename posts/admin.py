from django.contrib import admin

from posts.models import Review1_post, Review2_post, Review1_post_comment, Review2_post_comment, Review1_post_image, Review2_post_image

# Register your models here.

admin.site.register(Review1_post)
admin.site.register(Review2_post)

admin.site.register(Review1_post_comment)
admin.site.register(Review2_post_comment)

admin.site.register(Review1_post_image)
admin.site.register(Review2_post_image)

