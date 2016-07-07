from rest_framework import serializers
from locations.models import Location, LANGUAGE_CHOICES, STYLE_CHOICES


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')
