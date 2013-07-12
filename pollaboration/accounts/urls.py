from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from accounts import views
    
urlpatterns = patterns('',
    url(r'^login/$', views.login_view, name='login'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)