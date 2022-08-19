from django.contrib import admin

from .models import Parcel, ParcelShelf


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'creation_date', 'last_modification')


@admin.register(ParcelShelf)
class ParcelShelfAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'creation_date', 'last_modification')

