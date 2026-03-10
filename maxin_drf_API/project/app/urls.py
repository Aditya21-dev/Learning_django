from django.urls import path
from .views import *
urlpatterns = [
    path('stu_list/', StudentList.as_view(), name='Stu_list'),
    path('stu_Detail/<int:pk>/', StudentDetail.as_view(), name='Stu_Detail')
]