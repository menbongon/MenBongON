from django.contrib import admin

from django.urls import path, include

import accounts.views
import mypage.views
import menbongapp.views 
import posts.views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menbongapp.views.intro, name="intro"),
    path('home/', menbongapp.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('board/', include('posts.urls')),
    path('mypage/', mypage.views.mypage, name="mypage"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)