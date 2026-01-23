from django.shortcuts import render,redirect
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
    if req.method == 'POST':
        n = req.POST.get('user_name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        p = req.POST.get('password')
        user = KFC_User.objects.filter(email=e)

        if user:
            req.session['Ee'] = "email alredy exist"
            return redirect('registration')
        else:
            KFC_User.objects.create(user_name=n,email=e,contact=c,password=p)
            return redirect('login')
    msg = req.session.get('Ee','')
    return render(req,"registration.html",{'mseg':msg})

def login(req):
    if req.mehod == 'POST':
        e = req.POST.get("email")
    return render(req,"login.html")

