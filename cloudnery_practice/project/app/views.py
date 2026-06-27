from django.shortcuts import render
from .models import UserProfile
# Create your views here.

def landing(req):
    return render(req,"landing.html")

def form(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        img = req.FILES.get("img")

        user = UserProfile.objects.create(name = name , email = email , image = img)
        return render(req,"landing.html" , {"user" : user})
    
    return render(req,"form.html")