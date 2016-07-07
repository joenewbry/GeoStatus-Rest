from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer


@api_view(['GET', 'POST'])
def location_list(request, format=None):
    """
    List all locations, or create a new location
    """
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a location.
    """
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

