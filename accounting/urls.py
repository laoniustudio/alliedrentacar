from django.conf.urls import url
from .views import CaseList,logout_view,CaseListDetail,toPDF
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'accounting'

urlpatterns = [
    url(r'^$',login_required(CaseList.as_view()),name='caselist'),
    url(r'^logout$',logout_view,name='logout'),
    url(r'^(?P<pk>\d+)$',CaseListDetail.as_view(),name='casedetail'),
    url(r'^(?P<pk>\d+)/toPDF/$', toPDF, name='pdf'),
]
