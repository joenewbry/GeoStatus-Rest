from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from locations import views

urlpatterns = [
    url(r'^locations/$', views.location_list),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.location_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
