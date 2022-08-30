from datetime import datetime
from random import randint

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Parcel, ParcelShelf
from .serializers import ParcelSerializer, ParcelShelfSerializer
from .permissions import IsAuthorOrReadOnly, NoAdminUser


def code_generator(user):
    user = user

    date = datetime.now().date()
    date_normalizer = str(date).replace('-', '')

    time = datetime.now().time()
    time_normalizer = str(time)[:8].replace(':', '')

    rn = randint(1, 999999)

    return f'{user}00{rn}00{date_normalizer}00{time_normalizer}'


class ParcelsList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser, NoAdminUser)
    permission_classes = (NoAdminUser,)
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def perform_create(self, serializer):
        code = code_generator(user=self.request.user.id)
        serializer.save(owner=self.request.user, code=code)


class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.DjangoObjectPermissions,)
    permission_classes = (NoAdminUser,)
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    # def get_queryset(self):
    #     self.lookup_field = 'pk'
    #     print('LOOKUP_FIELD: ', self.lookup_field, flush=True)
    #     user = self.request.user
    #     print('USER: ', user, flush=True)
    #     return Parcel.objects.filter(owner=user)


class ParcelsShelfList(generics.ListCreateAPIView):
    queryset = ParcelShelf.objects.all()
    serializer_class = ParcelShelfSerializer


class ParcelShelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelShelf.objects.all()
    serializer_class = ParcelShelfSerializer
