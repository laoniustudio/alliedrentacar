from django.conf.urls import url
from .views import CaseList,logout_view
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'accounting'

urlpatterns = [
    url(r'^$',login_required(CaseList.as_view()),name='caselist'),
    url(r'^/logout$',logout_view,name='logout'),
]
