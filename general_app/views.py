from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_root(request, format=None):
    domain = request.build_absolute_uri()
    return Response({
        'parcels': reverse('parcels_list_view', request=request, format=format),
        'parcels-shelf': reverse('parcels-shelf_list_view', request=request, format=format),
        'registration': f'{domain}api/v1/dj-rest-auth/registration/',
        'login': f'{domain}api/v1/dj-rest-auth/login/',
        'logout': f'{domain}api/v1/dj-rest-auth/logout/',
    })
