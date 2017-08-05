from django.conf.urls import url
from .views import PostAPIViewGet,PostAPIViewPost,DamageInDetailAPIGetUpdate,MoreDamageInDetailAPIGet,MoreDamageInDetailAPIUpdate,PostAPIViewUpdate,PostAPIViewDelete


app_name = 'contentsAPI'

urlpatterns = [
    url(r'^create/$',PostAPIViewPost.as_view(),name='apicreate'),
    url(r'^allposts/$',PostAPIViewGet.as_view(),name='apiget'),
    url(r'^post/(?P<pk>\d+)/update$',PostAPIViewUpdate.as_view(),name='apiPostUpdate'),
    url(r'^post/(?P<pk>\d+)/delete$',PostAPIViewDelete.as_view(),name='apiPostDelete'),
    url(r'^moredamage/(?P<post>\d+)/$',MoreDamageInDetailAPIGet.as_view(),name='apiMoreDamage'),
    url(r'^alldamage/(?P<post>\d+)/$',DamageInDetailAPIGetUpdate.as_view(),name='apiAllDamage'),
    url(r'^moredamage/(?P<post>\d+)/(?P<id>\d+)/$',MoreDamageInDetailAPIUpdate.as_view(),name='apiMoreDamageUpdate'),

]
