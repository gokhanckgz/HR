from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
	url(r'^login/', include('login.urls')),
    url(r'^supplier/', include('supplier.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^company/', include('company.urls')),
	url(r'^logout/$', logout_view),	
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)