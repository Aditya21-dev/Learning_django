from django.shortcuts import render,redirect
from .models import MediaSubmission

# Create your views here.

def landing(req):
    return render(req,"landing.html")

def form_data(request):

    if request.method == "POST":

        MediaSubmission.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            title=request.POST.get("title"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
            video=request.FILES.get("video"),
            audio=request.FILES.get("audio"),
            document=request.FILES.get("document"),
        )

        print("Saved")

        return render(request,"form_data")

    return render(request, "landing.html")