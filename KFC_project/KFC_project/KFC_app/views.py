from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,"home.html")

def menu(req):
    return render(req,"menu.html")

def reward(req):
    return render(req,"reward.html")

def careers(req):
    return render(req,"careers.html")

def login(req):
    return render(req,"login.html")