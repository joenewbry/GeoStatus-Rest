from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from locations import views

urlpatterns = [
	url(r'^locations/$', views.user_status),
]