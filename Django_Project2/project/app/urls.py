from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    


    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    # payment 
    path("payment/", views.payment, name="payment"),
    path("payment-status", views.payment_status, name="payment-status"),



    path('Owner_dashboard/', views.admin, name='Admin_dashboard'),
    path('Add_dishes/', views.add_dishes, name='Add_dishes'),
    path('show_dishes/', views.show_dishes, name='show_dishes'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)