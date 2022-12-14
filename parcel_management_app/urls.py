from django.urls import path
from .views import ParcelsList, ParcelDetail, ParcelsShelfList, ParcelShelfDetail

urlpatterns = [
    path('parcels/', ParcelsList.as_view(), name='parcels_list_view'),
    path('parcels/<str:code>/', ParcelDetail.as_view(), name='parcels_detail_view'),
    path('parcels-shelf/', ParcelsShelfList.as_view(), name='parcels-shelf_list_view'),
    path('parcels-shelf/<int:pk>/', ParcelShelfDetail.as_view(), name='parcels-shelf_detail_view'),
]
