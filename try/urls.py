"""try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tapp.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^about/$',about),
    url(r'^detail/(\w+)/$',detail,name='detail'),
    url(r'^gallery/$',gallery),
    url(r'^gallery2/$',gallery2),
    url(r'^gallery3/$',gallery3),
    url(r'^gallery4/$',gallery4),
    url(r'^gallery5/$',gallery5),
    url(r'^gallery6/$',gallery6),
    url(r'^contact/$',contact),
    url(r'^menu/$',menu),
    url(r'^elements/$',elements),
    url(r'^blog-home/$',bloghome),
    url(r'^blog-single/$',blogsingle),
    url(r'^menu/(\w+)/$',item2,name='item2'),
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)
