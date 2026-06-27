from django.shortcuts import render,redirect
from .models import User , Todo
from django.contrib import messages
# Create your views here.

def landing(req):
    return render(req,"landing.html")

def registration(req):
    if req.method == 'POST':
        user_name = req.POST.get("name")
        user_email = req.POST.get("email")
        user_password = req.POST.get("password")

        check_email = User.objects.filter(email = user_email).first()

        if check_email:
            messages.error(req, "Email already exists")            
            return redirect("login")
        else:
            User.objects.create(name = user_name , email = user_email , password = user_password)
            messages.success(req, "Account created successfully. Please login.")
            return redirect("login")
    else:    
        return render(req,"registration.html")

def login(req):
    if req.method == 'POST':
        user_email = req.POST.get("email")
        user_password = req.POST.get("password")
        
        user_detail = User.objects.filter(email = user_email).first()

        if user_detail and user_password == user_detail.password:
            req.session["user_name"] = user_detail.name
            req.session["user_email"] = user_detail.email
            req.session["user_password"] = user_detail.password

            messages.success(req, "Account created successfully. And login succesfull..!.")
            return redirect("dashboard")
        else:
            return redirect("login")
    return render(req,"login.html")

def logout(req):
    req.session.flush()
    return redirect("login")


def dashboard(req):
    user_details = {
    "user_name" : req.session.get("user_name"),
    "user_email" : req.session.get("user_email")
    }
    return render(req,"dashboard.html",{"dashboard_content":True,"user_detail":user_details})

def todo_list(req):
    task_detail = Todo.objects.all()
    return render(req,"dashboard.html",{"todo_list":True , "task_detail":task_detail})

def add_task(req):
    if req.method == 'POST':
        task = req.POST.get("task")
        task_exist = Todo.objects.filter(task = task).first()

        if task_exist:
            messages.error(req, "Task already exists")
            return redirect("todo_list")
        else:
            Todo.objects.create(task = task)
            messages.success(req, "Task Added succesfull..!")
            return redirect("todo_list")
        
    messages.warning("Not empty task can't be listed !")
    return redirect("todo_list")
            
def delete_task(req,task_id):
    deleted_task = Todo.objects.get(id = task_id)
    deleted_task.delete()
    return redirect("todo_list")

def edit_task(req,task_id):
    task = Todo.objects.get(id=task_id)
    task_detail = Todo.objects.all()

    return render(req, "dashboard.html", {
        "todo_list": True,
        "task_detail": task_detail,
        "edit_task_obj": task
    })

def update_task(req, task_id):
    if req.method == "POST":
        task = Todo.objects.get(id=task_id)
        task.task = req.POST.get("task")
        task.save()
        messages.success(req, "Task updated successfully.")

    return redirect("todo_list")