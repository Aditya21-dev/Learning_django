from django.shortcuts import render

# Create your views here.

def home(req):
    context = {
        "name" : "Adidas",
        "age": 24,
        "marks": 91.45,
        "city": "Bhopal",
        "is_student": True,
        "fruits": ["Apple", "Banana", "Mango", "Orange"],
        "numbers": [10,20,30,40],
        "empty_list": []
    }

    return render(req , "home.html" , context)