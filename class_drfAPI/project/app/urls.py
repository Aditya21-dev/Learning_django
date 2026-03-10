
from django.urls import path
from .views import *
urlpatterns = [
    path('stu_list/', Stu_list.as_view(), name='Stu_list'),
    path('stu_Detail/<int:pk>/', Stu_Detail.as_view(), name='Stu_Detail')
]