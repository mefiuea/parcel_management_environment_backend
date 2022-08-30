from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Parcel, ParcelShelf


class ParcelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    code = serializers.ReadOnlyField()

    class Meta:
        model = Parcel
        fields = ('id', 'code', 'owner', 'name', 'contents', 'size', 'weight', 'contact', 'creation_date',
                  'last_modification')


class ParcelShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelShelf
        fields = ('id', 'owner', 'name', 'creation_date', 'last_modification', 'parcels')
