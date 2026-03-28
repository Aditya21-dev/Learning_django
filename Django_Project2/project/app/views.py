from django.shortcuts import render,redirect
from .models import User , Dishes
from django.contrib import messages
# Create your views here.

def home(req):
    return render(req,"Home.html")

def menu(req):
    type_filter = req.GET.get("type")

    if type_filter == "Veg":
        dishes = Dishes.objects.filter(type="Veg")
    elif type_filter == "Non-veg":
        dishes = Dishes.objects.filter(type="Non-Veg")
    else:
        dishes = Dishes.objects.all()

    return render(req, "Menu.html", {"dishes": dishes})

def cart(req):
    return render(req,"Cart.html")



def signup(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")
        address = req.POST.get("address")

        if password != confirm_password:
            messages.error(req, "password do not match")
            return render(req, "signup.html", {"error": "Passwords do not match"})

        if User.objects.filter(email=email).exists():
            messages.error(req, "Email already exists")
            return render(req, "signup.html")

        User.objects.create(name=name, email=email, password=password, address=address)

        return redirect("login")

    return render(req, "signup.html")



def login(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        if email == "admin@gmail.com" and password == "admin1234":
            req.session['admin'] = True
            return redirect("Admin_dashboard")  

        try:
            user = User.objects.get(email=email, password=password)

            req.session['user_id'] = user.id
            req.session['user_name'] = user.name

            return redirect("home")

        except User.DoesNotExist:
            messages.error(req, "Invalid email or password")
            return render(req, "login.html")

    return render(req, "login.html")



def logout(req):
    req.session.flush()
    return redirect("login")























def admin(req):
    return render(req,"Admin_dashboard.html" ,{"dashboard":True})

def add_dishes(req):
    if req.method == "POST":
        name = req.POST.get("name")
        price = req.POST.get("price")
        type = req.POST.get("type")
        image = req.FILES.get("image")

        Dishes.objects.create(
            name=name,
            price=price,
            type=type,
            image=image
        )

        from django.contrib import messages
        messages.success(req, "Dish Added Successfully")
        return render(req,"Admin_dashboard.html", {"Add_dishes": True}) 

    return render(req, "Admin_dashboard.html", {"Add_dishes": True})

def show_dishes(req):
    dishes = Dishes.objects.all()
    return render(req, "Admin_dashboard.html", {"Show_dishes": True,"dishes": dishes})