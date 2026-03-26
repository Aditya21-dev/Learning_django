from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,"Home.html")

def menu(req):
    return render(req,"Menu.html")

def cart(req):
    return render(req,"Cart.html")

def admin(req):
    return render(req,"Admin_dashboard.html")