from django.contrib import admin

from django.urls import path, include

import accounts.views
import mypage.urls
import menbongapp.views 
import posts.views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menbongapp.views.intro, name="intro"),
    path('home/', menbongapp.views.home, name="home"),
    path('menbong/', menbongapp.views.menbong, name="menbong"),
    path('admission/', menbongapp.views.admission, name="admission"),
    path('entrance_info/', menbongapp.views.entrance_info, name="entrance_info"),
    path('accounts/', include('accounts.urls')),
    path('board/', include('posts.urls')),
    path('mypage/',include('mypage.urls')),
    path('programmer/', menbongapp.views.programmer, name="programmer"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)