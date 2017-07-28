from django.conf.urls import url
from .views import PostAPIViewGet,PostAPIViewPost


app_name = 'contentsAPI'

urlpatterns = [
    url(r'^create/$',PostAPIViewPost.as_view(),name='apicreate'),
    url(r'^get/$',PostAPIViewGet.as_view(),name='apiget'),


]
