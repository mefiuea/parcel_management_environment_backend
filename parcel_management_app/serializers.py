from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Parcel, ParcelShelf


class ParcelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    code = serializers.ReadOnlyField()

    class Meta:
        model = Parcel
        fields = ('id', 'code', 'owner', 'name', 'contents', 'size', 'weight', 'contact', 'creation_date',
                  'last_modification')


class ParcelShelfSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    parcels = serializers.HyperlinkedRelatedField(many=True, read_only=False, view_name='parcels_detail_view',
                                                  # queryset=Parcel.objects.filter(owner=17)
                                                  queryset=Parcel.objects.all()
                                                  )

    class Meta:
        model = ParcelShelf
        fields = ('id', 'owner', 'name', 'creation_date', 'last_modification', 'parcels')
