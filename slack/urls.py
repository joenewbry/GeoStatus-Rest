from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from slack import views

urlpatterns = [
    url(r'^slack/$', views.user_status),
]

urlpatterns = format_suffix_patterns(urlpatterns)
