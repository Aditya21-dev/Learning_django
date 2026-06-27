from django.shortcuts import render

# Create your views here.

def form(req):
    # data = req.get.post

    return render (req , "form.html")




def show(req):
    return render(req , "show.html")
