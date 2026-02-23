from django.shortcuts import render,redirect
from .models import Appointment
# Create your views here.

def home(req):
    return render(req,"home.html")

def save_appointment(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        phone = req.POST.get("phone")
        gender = req.POST.get("gender")
        doctor = req.POST.get("doctor")
        date = req.POST.get("date")
        problem = req.POST.get("problem")
        Appointment.objects.create(name=name,email=email,phone=phone,gender=gender,doctor=doctor,date=date,problem=problem)
        return redirect("appointment_recipt")
        
    return render(req, "home.html")

def appointment_recipt(req):
    appointment_slip = Appointment.objects.all()
    return render(req,"appointment_slip.html",{"appointment_slip_detail":appointment_slip})