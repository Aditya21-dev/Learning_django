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

        if password2 == req.session.get("password"):
            return render(req,"landing.html")
        
    return render(req,"login.html")


def verify_email(req):
    if req.method == 'POST':
        email = req.POST.get("email")
        
        if email != req.session.get("email"):
            msg = "wrong email"
            return render(req,"login.html",{"verify_email":True,"msg":msg}) 
        else:
            otp = random.randint(1111 , 9999)
            req.session["otp"] = otp  
            send_mail(
                "Your verification OTP",
                f"Your OTP is:\n{otp}",
                "adityadas0217@gmail.com",
                [req.session.get("email")],
            )
            return(render,"login.html",{"conform_otp":True})
    return render(req,"login.html",{"verify_email":True})