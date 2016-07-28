from locations.models import Location
from locations.models import Context
from locations.models import Status
from locations.models import GeoStatus
from locations.serializers import LocationSerializer
from locations.serializers import UserSerializer
from locations.serializers import GeoStatusSerializer

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from locations.permissions import IsOwnerOrReadOnly


class LocationList(generics.ListCreateAPIView):
    """
    List all locations, or create a new location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                         IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GeoStatusList(generics.ListCreateAPIView):
    """
    List all geo statuses, or create a new geo status
    """
    queryset = GeoStatus.objects.all()
    serializer_class = GeoStatusSerializer

class GeoStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update, or delete a geo status instance.
    """
    queryset = GeoStatus.objects.all()
    serializer_class = GeoStatusSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
