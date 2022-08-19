from django.urls import path
from .views import ParcelsList, ParcelDetail

urlpatterns = [
    path('parcels/', ParcelsList.as_view()),
    path('parcels/<int:pk>/', ParcelDetail.as_view()),
]
