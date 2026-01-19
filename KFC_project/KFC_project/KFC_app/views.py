from django.shortcuts import render
from .models import KFC_User
# Create your views here.

def home(req):
    return render(req,"home.html")

def menu(req):
    return render(req,"menu.html")

def reward(req):
    return render(req,"reward.html")

def careers(req):
    return render(req,"careers.html")

def registration(req):
    return render(req,"registration.html")

def login(req):
    return render(req,"login.html")

def formdata(req):
    if req.method=='POST':
       n = req.POST.get('user_name')
       e = req.POST.get('email')
       p = req.POST.get('password')
    print(n,e,p)
   
    KFC_User.objects.create(user_name=n,email=e,password=p)
