from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^services/$', services , name="Selections"),
    url(r'^profile/$', profile , name="Profile"),
    url(r'^profile/credit_transfer', credit_transfer , name="credit_transfer"),
    url(r'^services/service_choose/(\d+)', service_choose, name="service_choose"),
    url(r'^service_info/service_choose/(\d+)', service_choose, name="service_choose"),
    url(r'^services/service_leave/(\d+)', service_leave, name="service_leave"),
    url(r'^service_info/service_leave/(\d+)', service_leave, name="service_leave"),
    url(r'^services/service_info/(\d+)', service_info, name="service_info"),
]
