from rest_framework.decorators import api_view
from rest_framework.response import Response

# From http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# Could use class based views instead
# Create your views here.


@api_view(['GET'])
def user_status(request):
    """
    Get current user status
    """
    return Response("Hello World")
