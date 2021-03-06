from django.conf.urls import url
from .views import (PostAPIViewGet,PostAPIViewPost,DamageInDetailAPIGetUpdate,MoreDamageInDetailAPIGet,
MoreDamageInDetailAPIUpdate,PostAPIViewUpdate,PostAPIViewDelete,UserGet,PermissionGet,InvitationGet,CarGet,CarDetailGet)


app_name = 'contentsAPI'

urlpatterns = [
    url(r'^create/$',PostAPIViewPost.as_view(),name='apicreate'),
    url(r'^allposts/$',PostAPIViewGet.as_view(),name='apiget'),
    url(r'^post/(?P<pk>\d+)/update$',PostAPIViewUpdate.as_view(),name='apiPostUpdate'),
    url(r'^post/(?P<pk>\d+)/delete$',PostAPIViewDelete.as_view(),name='apiPostDelete'),
    url(r'^moredamage/(?P<post>\d+)/$',MoreDamageInDetailAPIGet.as_view(),name='apiMoreDamage'),
    url(r'^alldamage/(?P<post>\d+)/$',DamageInDetailAPIGetUpdate.as_view(),name='apiAllDamage'),
    url(r'^moredamage/(?P<post>\d+)/(?P<id>\d+)/$',MoreDamageInDetailAPIUpdate.as_view(),name='apiMoreDamageUpdate'),
    url(r'^users/$',UserGet.as_view(),name='apiUsers'),
    url(r'^users/permission/(?P<pk>\d+)/$',PermissionGet.as_view(),name='apiPermission'),
    url(r'^users/invitation/$',InvitationGet.as_view(),name='apiInvitation'),
    url(r'^cars/$',CarGet.as_view(),name='apiCar'),
    url(r'^cars/(?P<pk>\d+)$',CarDetailGet.as_view(),name='apiCarDetail'),

]
