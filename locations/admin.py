from django.contrib.gis import admin
from .models import Context, Location

admin.site.register(Context, admin.OSMGeoAdmin)
admin.site.register(Location, admin.OSMGeoAdmin)

