"""WebApp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from API import views as local_views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', local_views.get_auth_token, name='login'),
    url(r'^logout/$', local_views.logout_user, name='logout'),
    url(r'^users/$', local_views.UserRegistration.as_view()),
]
