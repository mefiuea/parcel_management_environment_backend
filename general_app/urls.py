from django.urls import path

from general_app.views import api_root

app_name = 'parcel_management_app'

urlpatterns = [
    path('', api_root, name='general_view'),
]
