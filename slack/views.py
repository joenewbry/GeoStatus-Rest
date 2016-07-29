from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from locations.models import GeoStatus
import requests

# From http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# Could use class based views instead
# Create your views here.


@api_view(['POST', 'GET'])
def user_status(request):
    """
    Get current user status
    """
    # TODO: add some basic validation
    username = request.data['text']
    geostatus = GeoStatus.objects.filter(username=username).last()
    if request.method == 'GET':
    	return Response(request.data)



    if geostatus is None:
        payload = {'text': 'No GeoStatus found for ' + request.data['text']}
        return Response(request.data)
    else:
        username = geostatus.username
        verb = geostatus.verb
        location = geostatus.location
        text_response = "" + username + " " + verb + " " + location
        payload = {'text': text_response}
        return Response(request.data)

"""
Data posted by slack to external url
------------------------------------
token=gIkuvaNzQIHg97ATvDxqgjtO
team_id=T0001
team_domain=example
channel_id=C2147483705
channel_name=test
user_id=U2147483697
user_name=Steve
command=/weather
text=94070
response_url=https://hooks.slack.com/commands/1234/5678
"""