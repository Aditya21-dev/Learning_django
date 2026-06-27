from django.shortcuts import render
from .models import  User
from django.core.mail import send_mail
import random
# Create your views here.

def landing(req):
    return render(req,"landing.html")

def register(req):

    if req.method == "POST":

        name = req.POST.get("name")
        email = req.POST.get("email")
        password = req.POST.get("password")

        email_check = User.objects.filter(email=email)

        if email_check.exists():
            msg = "Email already exists"
            return render(req, "register.html", {"msg": msg})

        else:
            User.objects.create(name=name, email=email, password=password)

            req.session["email"] = email
            req.session["password"] = password

            return render(req, "login.html", {"name": name, "email": email , "login":True})

    return render(req, "register.html",{"login":True})


def login(req):
    # email = req.session.get("email")
    if req.method == 'POST':
        password2 = req.POST.get("password")
        email = req.POST.get("email")

        if password2 == req.session.get("password") and email == req.session.get("email"):
            return render(req,"landing.html")
        else:
            msg = "something went wrong !"
            return render(req,"login.html",{"login":True , "msg":msg})
    return render(req,"login.html",{"login":True})


def verify_email(req):
    if req.method == 'POST':
        email = req.POST.get("email")
        
        email_check = User.objects.filter(email=email)

        if email_check.exists():
            otp = random.randint(1111 , 9999)
            req.session["otp"] = str(otp)  
            req.session["email"] = email 
            send_mail(
                "Your verification OTP",
                f"Your OTP is:\n{otp}",
                "adityadas0217@gmail.com",
                [email],
            )
            return render(req,"login.html",{"verify_OTP":True})
             
        else:
            msg = "wrong email"
            return render(req,"login.html",{"verify_email":True,"msg":msg})
            
    return render(req,"login.html",{"verify_email":True})


def verify_OTP(req):
    if req.method == 'POST':
        otp = req.POST.get("otp")
        
        if otp != req.session.get("otp"):
            msg = "wrong OTP"
            return render(req,"login.html",{"verify_OTP":True,"msg":msg}) 
        else:
            return render(req,"login.html",{"new_password":True})
    return render(req,"login.html",{"verify_OTP":True})


def new_password(req):

    if req.method == "POST":

        new_password = req.POST.get("new_password")
        conform_password = req.POST.get("conform_password")

        if new_password == conform_password:

            User.objects.filter(email=req.session.get("email")).update(password = new_password)

            return render(req,"login.html",{"login":True})

        else:
            msg = "Password not match"
            return render(req,"login.html",{"new_password":True,"msg":msg})

    return render(req,"login.html",{"new_password":True})