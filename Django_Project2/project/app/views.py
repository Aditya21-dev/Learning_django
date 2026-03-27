from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,"Home.html")

def menu(req):
    return render(req,"Menu.html")

def cart(req):
    return render(req,"Cart.html")

def admin(req):
    return render(req,"Admin_dashboard.html" ,{"dashboard":True})

def add_dishes(req):
    return render(req,"Admin_dashboard.html" ,{"Add_dishes":True})

def save_dishes(req):
    return render(req,"Admin_dashboard.html" ,{"dashboard":True})
    pass

def show_dishes(req):
    return render(req,"Admin_dashboard.html" ,{"Show_dishes":True})

# path('Add_dishes/', views.add_dishes, name='Add_dishes'),
#     path('save_dishes/', views.save_dishes, name='save_dishes'),
#     path('show_dishes/', views.show_dishes, name='show_dishes'),