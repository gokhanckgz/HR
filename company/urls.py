from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^$', index),
	url(r'^profile', profile, name="Profile"),
	url(r'^employes/$', employes),
	url(r'^employes/emp_add/$', emp_add),
	url(r'^employes/emp_delete/(\d+)', emp_delete , name="emp_delete"),
	url(r'^employes/emp_edit/(\d+)', emp_edit , name="emp_edit"),
	url(r'^services/$', services),
	url(r'^services/service_info/(\d+)', service_info),
	url(r'^services/service_choose/(\d+)', service_choose),
	url(r'^services/service_delete/(\d+)', service_delete),
	url(r'^service_use/(\d+)', employe_service_use),
	url(r'^employe_info/(\d+)', employe_info, name="company_employe_info"),
	url(r'^employe_info/service_delete/(\d+)/(\d+)', employe_service_delete, ),
]
