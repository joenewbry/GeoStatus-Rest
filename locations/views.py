from locations.models import Location
from locations.serializers import LocationSerializer
from rest_framework import generics


class LocationList(generics.ListCreateAPIView):
    """
    List all locations, or create a new location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
