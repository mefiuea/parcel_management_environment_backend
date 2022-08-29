from rest_framework.decorators import api_view
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'parcels': reverse('parcels_list_view', request=request, format=format),
        'parcels-shelf': reverse('parcels-shelf_view', request=request, format=format),
    })
