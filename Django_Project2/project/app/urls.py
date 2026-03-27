from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),


    path('Owner_dashboard/', views.admin, name='Admin_dashboard'),
    path('Add_dishes/', views.add_dishes, name='Add_dishes'),
    path('save_dishes/', views.save_dishes, name='save_dishes'),
    path('show_dishes/', views.show_dishes, name='show_dishes'),
]