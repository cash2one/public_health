from django.conf.urls import patterns, url
from backend import views


urlpatterns = patterns('',
                       url(r'^login/$', views.login),
                       url(r'^register/$', views.register),
)