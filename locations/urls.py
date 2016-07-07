from django.conf.urls import url
from locations import views

urlpatterns = [
    url(r'^locations/$', views.location_list),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.location_detail),
]
