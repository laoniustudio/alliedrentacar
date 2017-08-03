from django.conf.urls import url
from .views import PostAPIViewGet,PostAPIViewPost,PostDetailAPIGet


app_name = 'contentsAPI'

urlpatterns = [
    url(r'^create/$',PostAPIViewPost.as_view(),name='apicreate'),
    url(r'^allposts/$',PostAPIViewGet.as_view(),name='apiget'),
    url(r'^damage/(?P<post>\d+)/$',PostDetailAPIGet.as_view(),name='apidetail'),


]
