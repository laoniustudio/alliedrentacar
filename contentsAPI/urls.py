from django.conf.urls import url
from .views import PostAPIViewGet,PostAPIViewPost,DamageInDetailAPIGet,MoreDamageInDetailAPIGet,DamageInDetailAPIUpdate


app_name = 'contentsAPI'

urlpatterns = [
    url(r'^create/$',PostAPIViewPost.as_view(),name='apicreate'),
    url(r'^allposts/$',PostAPIViewGet.as_view(),name='apiget'),
    url(r'^post/(?P<id>\d+)/$',MoreDamageInDetailAPIGet.as_view(),name='apipostget'),
    url(r'^alldamage/(?P<post>\d+)/update/$',DamageInDetailAPIUpdate.as_view(),name='apiAllDamageUpdate'),
    url(r'^alldamage/(?P<post>\d+)/$',DamageInDetailAPIGet.as_view(),name='apiAllDamage'),



]
