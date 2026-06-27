from django.shortcuts import render
from django.http import JsonResponse
from .models import Teacher , Department , Order , Customer

# Create your views here.

def landing(req):
    return render(req,"landing.html")

def forward_access(req,id):
    Teachers = Teacher.objects.get(id = id)

    departments = Teachers.department  #Forword Access 

    data = {
        "teacher_name": Teachers.name,
        "subject": Teachers.subject,
        "department_name": departments.name,
        "department_building": departments.building,
        "hod": departments.hod_name
    }
    return render(req,"result.html",{"data":data})


def result(req):
    return render(req,"result.html")


def backword_access(req,id):
    department = Department.objects.get(id=id)

    teachers = department.teachers  # Reverse Access

    context = {
        "department": department,
        "teachers": teachers
    }

    return render(req, "result.html", {"context":context})



def forward_access_om(req):
    orders = Order.objects.select_related('customer').all()

    data = []

    for order in orders:
        data.append({
            "order_id": order.id,
            "product": order.product_name,
            "customer_name": order.customer.name,
            "customer_email": order.customer.email,            
        })
    
    return render(req,"result.html", {"om_data":data})

def backword_access_om(req):
    customers = Customer.objects.prefetch_related('orders')
    return render(req, "result.html", {"customers": customers})

