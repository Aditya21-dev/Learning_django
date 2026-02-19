from django.shortcuts import render,redirect
from .form import UserModels

# Create your views here.

def landing(req):
    return render(req,"landing.html")


def register(request):
    form = UserModels()
    return render(request, "register.html", {"form": form})



def register(request):
    if request.method == "POST":
        form = UserModels(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = UserModels()
    return render(request, "register.html", {"form": form})



def success(request):
 return render(request, "success.html")

