from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^$', index),
	url(r'^services/$', services),
	url(r'^customers/$', customers),
	url(r'^profile', profile , name="Profile"),
	url(r'^services/service_info/(\d+)', service_info, name="service_info"),
	url(r'^customers/employe_info/(\d+)', employe_info, name="employe_info"),
	url(r'^service_use/(\d+)', service_use, name="service_use"),
] + static(settings.STATIC_URL,)
