from django.shortcuts import render
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail

# Create your views here.

def landing(req):
    if req.method=='POST':
        emp_name=req.POST.get('emp_name')
        emp_email=req.POST.get('emp_email')
        emp_department=req.POST.get('emp_department')
        emp_role=req.POST.get('emp_role')
        emp_password=req.POST.get('emp_pass')
        
        Employee.objects.create(name=emp_name,email=emp_email,department=emp_department,role=emp_role,password=make_password(emp_password))
        User.objects.create(username=emp_name,email=emp_email,password=make_password(emp_password))
        req.session['email']=emp_email
        
        
        
        return render(req,'jwt_token.html')
    return render(req,'landing.html')

def jen_token(req):
    e=req.session.get('email')
    user=User.objects.get(email=e)
    jwt_token=Token.objects.create(user=user)
    print(jwt_token)
    send_mail(
            "JWT token",
            f"Your jwt token: {jwt_token}",
            "adityadas0217@gmail.com",     
            [e],                    
            fail_silently=False,
        )
    return render(req,'landing.html')
    