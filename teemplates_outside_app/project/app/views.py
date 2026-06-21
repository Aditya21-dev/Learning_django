from django.shortcuts import render

# Create your views here.

import templates

def test(req):
    return render(req,'test.html')