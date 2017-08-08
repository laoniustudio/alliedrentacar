"""allied URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import homesignin,signup
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from django.conf import settings # only for develop
from django.conf.urls.static import static,serve# only for develop


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',homesignin,name='home'),
    url(r'^dashboard/',include('accounting.urls')),
    url(r'^api/',include('contentsAPI.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^signup/$', signup,name='signup'),
    url(r'^invitations/', include('invitations.urls', namespace='invitations')),




    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)# only for develop

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


