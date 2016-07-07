from rest_framework import serializers
from locations.models import Location, LANGUAGE_CHOICES, STYLE_CHOICES


class LocationSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated
        data.
        """
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude',
                                                instance.longitude)
        instance.save()
        return instance
