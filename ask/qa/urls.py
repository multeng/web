from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^(?P<num>\d+)/$', views.test),
]
