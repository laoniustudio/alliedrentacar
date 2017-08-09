from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from .views import invite,invite_accept

app_name = 'invitation'

urlpatterns = [
    url(r'^invite/$',login_required(invite),name='sendInvite'),
    url(r'^accept/(?P<token>[0-9A-Za-z_\-]+)/$',invite_accept,name='acceptInvite'),
]
