from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index  , name='index'),
    url(r'^package/(?P<id>\d+)$', views.plans  , name='plan'),
    url(r'^packages', views.packages  , name='packages'),
    url(r'^contacted', views.contacted , name='contacted'),
    url(r'^booked', views.booked , name='booked'),
    url(r'^makemyowntripbooked', views.makemyowntripbooked , name='makemyowntripbooked'),
    url(r'^makemyowntrip', views.makemyowntrip , name='makemyowntrip'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)