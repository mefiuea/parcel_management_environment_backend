from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Parcel, ParcelShelf


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('owner', 'name', 'contents', 'size', 'weight', 'contact', 'creation_date', 'last_modification')
