"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home import views


urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('content/', include('content.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('content/<int:id>/<slug:slug>/', views.hakkımızda, name='hakkımızda'),
    path('menu/<int:id>/', views.menu, name='menu'),
    path('referans/', views.referans, name='referans'),
    path('iletişim/', views.iletişim, name='iletişim'),
    path('siteHak/', views.siteHak, name='siteHak'),
    path('duyuru/', views.duyuru, name='duyuru'),
    path('etkinlik/', views.etkinlik, name='etkinlik'),
    path('anons/<int:id>/<slug:slug>/', views.duyuru_Detay, name='duyuru_Detay'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('kayıtol/', views.join_view, name='join_view'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)