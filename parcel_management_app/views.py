from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Parcel
from .serializers import ParcelSerializer


class ParcelsList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    # def get_queryset(self):
    #     self.lookup_field = 'pk'
    #     print('LOOKUP_FIELD: ', self.lookup_field, flush=True)
    #     user = self.request.user
    #     print('USER: ', user, flush=True)
    #     return Parcel.objects.filter(owner=user)
