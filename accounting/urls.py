from django.conf.urls import url
from .views import CaseList,logout_view,CaseListDetail,toPDF,ToastShow,GetUsers,PermissionToast,GetCars,AddCar
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'accounting'

urlpatterns = [
    url(r'^$',login_required(CaseList.as_view()),name='caselist'),
    url(r'^logout$',login_required(logout_view),name='logout'),
    url(r'^(?P<pk>\d+)$',CaseListDetail.as_view(),name='casedetail'),
    url(r'^(?P<pk>\d+)/toPDF/$', toPDF, name='pdf'),
    url(r'^toast-template/$', ToastShow.as_view(), name='toast'),
    url(r'^toast_permission/$', PermissionToast.as_view(), name='toastPermission'),
    url(r'^users/$', GetUsers.as_view(), name='users'),
    url(r'^cars/$', GetCars.as_view(), name='cars'),
    url(r'^cars/create$', AddCar.as_view(), name='carCreate'),
]
