from django.shortcuts import render,redirect
from django.contrib import messages
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


def registration(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        password = request.POST.get("password")
        check_email = KFC_User.objects.filter(email=email)
        
        if check_email:
            messages.error(request, "Email already registered. Please login.")
            return render(request, "registration.html")

        KFC_User.objects.create(user_name=user_name,email=email,contact=contact,password=password)

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")   

    return render(request, "registration.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = KFC_User.objects.get(email=email, password=password)

            # sirf naam session me
            request.session["user_name"] = user.user_name
            request.session["user_email"] = user.email
            request.session["user_password"] = user.password
            messages.success(request, "Welcome back")
            return redirect("home")
            re
        except KFC_User.DoesNotExist:
            return render(request, "login.html")

    return render(request, "login.html")


def logout(request):
    request.session.flush()
    return redirect("home")




# -----------------ADMIN---------------#


def admin_dashboard(req):
    return render(req,"admin_dashboard.html")


def users(req):
    
    return render(req, "admin_dashboard.html", {"users": True})


def add_department(req):
    return render(req, "admin_dashboard.html", {"add_department": True})


def show_departments(req):
    return render(req, "admin_dashboard.html", {"show_departments": True})


def add_employee(req):
    return render(req, "admin_dashboard.html", {"add_employee": True})


def show_employees(req):
    return render(req, "admin_dashboard.html", {"show_employees": True})
