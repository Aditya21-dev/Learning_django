from django.urls import path
from .views import *
urlpatterns = [
    path('BookingList/', BookingList.as_view(), name='BookingList'),
    path('BookingDetail/<int:pk>/', BookingDetail.as_view(), name='BookingDetail')
]