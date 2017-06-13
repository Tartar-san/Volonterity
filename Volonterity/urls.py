"""Volonterity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from volonter.views import *

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', main_page, name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^event_inside/$', event_inside),
    url(r'^event_outside/$', event_outside),
    url(r'^organization_inside/$', organization_inside),
    url(r'^organization_outside/$', organization_outside),
    url(r'^enter/$', auth_views.login),
    url(r'^about_us/$', about_us),
    url(r'^our_team/$', our_team),
    url(r'^search/$', search),
    url(r'^user_inside/$', user_inside),
    url(r'^user_outside/$', user_outside),
    url(r'^not_available/$', custom404_view)
    ]