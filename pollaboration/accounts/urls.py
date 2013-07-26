from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from accounts import views
    
urlpatterns = patterns('',
    url(r'^login_view/$', views.login_view, name='login'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^logout_view/$', views.logout_view, name='logout'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^facebook_login_success/$', views.facebook_login_success, name='facebook_login_success'),
    url(r'^connect_facebook_account/$', views.connect_facebook_account, name='connect_facebook_account'),
)