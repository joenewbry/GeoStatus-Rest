from rest_framework.decorators import api_view
from rest_framework.response import Response
from locations.models import Status

# From http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# Could use class based views instead
# Create your views here.


@api_view(['GET'])
def user_status(request):
    """
    Get current user status
    """
    most_recent_status = Status.last().context.name
    return Response(most_recent_status)
