from rest_framework import serializers
from .models import Parcel, ParcelShelf


def hyperlinked_related_field_by_owner(model, view_name, owner):
    return serializers.HyperlinkedRelatedField(
        many=True,
        view_name=view_name,
        queryset=model.objects.filter(owner=owner),
        lookup_field='code'
    )


class ParcelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    code = serializers.ReadOnlyField()
    code_URL = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='parcels_detail_view',
        lookup_field='code'
    )

    class Meta:
        model = Parcel
        fields = ('id', 'code', 'code_URL', 'owner', 'name', 'contents', 'size', 'weight', 'contact', 'creation_date',
                  'last_modification')


class ParcelShelfSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    parcels = serializers.HyperlinkedRelatedField(many=True,
                                                  read_only=False,
                                                  view_name='parcels_detail_view',
                                                  queryset=Parcel.objects.all()
                                                  )

    def get_fields(self):
        fields = super().get_fields()

        owner = self.context['request'].user
        fields['parcels'] = hyperlinked_related_field_by_owner(
            Parcel, 'parcels_detail_view', owner)

        return fields

    class Meta:
        model = ParcelShelf
        fields = ('id', 'owner', 'name', 'creation_date',
                  'last_modification', 'parcels')
