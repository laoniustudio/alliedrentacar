from django.conf.urls import url
from .views import CaseList

app_name = 'accounting'

urlpatterns = [
    url(r'^$',CaseList.as_view(),name='caselist'),
]
