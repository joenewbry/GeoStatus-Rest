from rest_framework import serializers
from django.contrib.auth.models import User
from locations.models import Location, LANGUAGE_CHOICES, STYLE_CHOICES, GeoStatus

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude', 'owner')

class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True,
                                                   queryset=Location.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class GeoStatusSerializer(serializers.ModelSerializer):

    
	class Meta:
		model = GeoStatus
		fields = ('location', 'device_type', 'verb', 'username', 'message', 'url')
