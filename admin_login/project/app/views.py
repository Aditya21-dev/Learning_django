from django.shortcuts import render , redirect
from .models import User
# Create your views here.

def home(req):
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = User.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password_1
        }
        return render(req,'home.html',{'data':data})
    return render(req,"home.html")

def about(req):
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = User.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password_1
        }
        return render(req,'about.html',{'data':data})
    return render(req,"about.html")

def servis(req):
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = User.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password_1
        }
        return render(req,'servis.html',{'data':data})
    return render(req,"servis.html")

def register(req):

    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        p1 = req.POST.get('password_1')
        p2 = req.POST.get('password_2')
        print(n,e,c,p1,p2)
        user = User.objects.filter(email=e)

        if user:
            # return render(req,'login.html',{"msg":"email alredy exist"})
            req.session['x'] = "email alredy exist"
            return redirect('login')
        else:
            User.objects.create(name=n,email=e,contact=c,password_1=p1,password_2=p2)
            return redirect('login')
    x = req.session.get('x','')
    return render(req,"register.html",{'x':x})

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e,p)
        if e == 'admin@gmail.com' and p == 'admin123':
            req.session['admin_email'] = e
            req.session['admin_password'] = p
            req.session['admin_name'] = 'admin'
            return redirect('dashboard')
        
        user = User.objects.filter(email=e)
        if user:
            userdata = User.objects.get(email = e)
            if p == userdata.password_1:
                id = userdata.id
                req.session['user_id']=id
                name = userdata.name
                req.session['user_name']=name
                email = userdata.email
                req.session['user_email']=email
                return redirect('dashboard')
            else:
                req.session['y']="Email and password not match"
                return redirect('login')
        else:
            req.session['x']="Email Not Register"
            return redirect('register')
    y = req.session.get('y','')    
    return render(req,'login.html',{'y':y})

def dashboard(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
        a_email = req.session['admin_email']
        a_password = req.session['admin_password']
        a_name= req.session['admin_name']
        a_data = {
            "name" : a_name,
            "email" : a_email,
            "password" : a_password,

        }
        return render(req,'admin_dashboard.html',{'data':a_data})
    
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = User.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password_1
        }
        return render(req,'dashboard.html',{'data':data})
    else:
        return redirect('login')
    

def logout(req):

    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')