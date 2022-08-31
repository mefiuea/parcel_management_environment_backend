from datetime import datetime
from random import randint

from rest_framework import generics
from .models import Parcel, ParcelShelf
from .serializers import ParcelSerializer, ParcelShelfSerializer
from .permissions import IsAdminOrRegularUser


def code_generator(user):
    user = user

    date = datetime.now().date()
    date_normalizer = str(date).replace('-', '')

    time = datetime.now().time()
    time_normalizer = str(time)[:8].replace(':', '')

    rn = randint(1, 999999)

    return f'{user}00{rn}00{date_normalizer}00{time_normalizer}'


class ParcelsList(generics.ListCreateAPIView):
    # queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def get_queryset(self):
        user = self.request.user
        if bool(user and user.is_staff and user.is_admin):
            return Parcel.objects.all()
        else:
            return Parcel.objects.filter(owner=user)

    def perform_create(self, serializer):
        code = code_generator(user=self.request.user.id)
        serializer.save(owner=self.request.user, code=code)


class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    lookup_field = 'code'
    permission_classes = (IsAdminOrRegularUser,)


class ParcelsShelfList(generics.ListCreateAPIView):
    # queryset = ParcelShelf.objects.all()
    serializer_class = ParcelShelfSerializer
    lookup_field = 'code'

    def get_queryset(self):
        user = self.request.user
        if bool(user and user.is_staff and user.is_admin):
            return ParcelShelf.objects.all()
        else:
            return ParcelShelf.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ParcelShelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelShelf.objects.all()
    serializer_class = ParcelShelfSerializer
