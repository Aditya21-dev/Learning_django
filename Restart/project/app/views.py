from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
# Create your views here.

def landing(req):
    return render(req,"landing.html")

def registration(req):
    if req.method == 'POST':
        user_name = req.POST.get("name")
        user_email = req.POST.get("email")
        user_password = req.POST.get("password")

        check_email = User.objects.filter(email = user_email).first()

        if check_email:
            messages.error(req, "Email already exists")            
            return redirect("login")
        else:
            User.objects.create(name = user_name , email = user_email , password = user_password)
            messages.success(req, "Account created successfully. Please login.")
            return redirect("login")
    else:    
        return render(req,"registration.html")

def login(req):
    if req.method == 'POST':
        user_email = req.POST.get("email")
        user_password = req.POST.get("password")
        
        user_detail = User.objects.filter(email = user_email).first()

        if user_detail and user_password == user_detail.password:
            req.session["user_name"] = user_detail.name
            req.session["user_email"] = user_detail.email
            req.session["user_password"] = user_detail.password

            messages.success(req, "Account created successfully. And login succesfull..!.")
            return redirect("dashboard")
        else:
            return redirect("login")
    return render(req,"login.html")

def logout(req):
    req.session.flush()
    return redirect("login")




def dashboard(req):
    user_details = {
    "user_name" : req.session.get("user_name"),
    "user_email" : req.session.get("user_email")
    }
    return render(req,"dashboard.html",{"dashboard_content":True,"user_detail":user_details})

def todo_list(req):
    return render(req,"dashboard.html",{"todo_list":True})