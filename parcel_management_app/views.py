from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Parcel
from .serializers import ParcelSerializer


class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

