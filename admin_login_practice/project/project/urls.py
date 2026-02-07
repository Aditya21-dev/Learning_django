"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('servis/',views.servis,name='servis'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),

    

    # ADMIN -------------------------- #
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_department/', views.add_department, name='add_department'),
    path('save_department/', views.save_department, name='save_department'),
    path('show_departments/', views.show_departments, name='show_departments'),

    path('add_employee/', views.add_employee, name='add_employee'),
    path('save_employee/', views.save_employee, name='save_employee'),
    path('show_employees/', views.show_employees, name='show_employees'),
    path('show_queries/', views.show_queries, name='show_queries'),

    path('reply_query/<int:q_id>/', views.reply_quer, name='reply_query'),




    # EMPLOYEE -------------------------- #
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    path('Queries/', views.Queries, name='Queries'),
    path('Queries/raise/', views.raise_query, name='raise_query'),
    path('Queries/total/', views.total_queries, name='total_queries'),
    path('Queries/solved/', views.solved_queries, name='solved_queries'),
    path('Queries/pending/', views.pending_queries, name='pending_queries'),

    path('save_query/', views.save_query, name='save_query'),
    path('edit_query/<int:q_id>', views.edit_query, name='edit_query'),
    path("update-query/<int:q_id>/", views.update_query, name="update_query"),
    path('delete_query/<int:q_id>', views.delete_query, name='delete_query'),
    
]
