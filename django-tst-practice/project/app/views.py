from django.shortcuts import render,redirect
from .models import User,Task
from .form import UserModels,LoginForm

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
            return render(request,"login.html",{"login":True})
    else:
        form = UserModels()
    
    return render(request, "register.html", {"form": form})



def login(req):
    form = LoginForm(req.POST or None)

    if req.method =="POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        user = User.objects.filter(email = email)
        
        if user:
            take_user = User.objects.get(email=email)

            if email == take_user.email and password == take_user.password :
                req.session["user_id"] = take_user.id
                return redirect("dashboard")   
        else:
            return render("login",{"login",True})
            
    return render(req, "login.html", {"form": form , "login":True})
            

def dashboard(req):
    user_details = User.objects.get(id=req.session.get("user_id"))
    return render(req, "dashboard.html", {"user_details": user_details})


def logout(req):
    req.session.flush()
    return redirect("login",{"login":True})


def forgot_password(req):
    return render(req,"login.html",{"forgot_password":True})

def check_email(req):
    # method
    pass

def check_OTP(req):
    pass

def New_Password(req):
    pass


def add_task(req):
    if req.method == 'POST':
        task_detail = req.POST.get("task")
        Task.objects.create(task = task_detail)
        task_d = Task.objects.all()
        print(task_d)
        return render(req,"dashboard.html",{"task_list":True ,"task_d":task_d})
    return redirect("dasboard")