from django.urls import path
from .views import ParcelList

urlpatterns = {
    path('parcels/', ParcelList.as_view()),
}
