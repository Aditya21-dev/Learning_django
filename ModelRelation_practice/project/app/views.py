from django.shortcuts import render
from django.http import JsonResponse
from .models import Teacher , Department

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