from django.shortcuts import render, redirect
from .models import User, Department , Employee
from .models import Employee, Department
from django.contrib import messages
from django.core.mail import send_mail
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
            messages.error(req, "Email already exists")    
            return redirect('login')
        else:
            User.objects.create(name=n,email=e,contact=c,password_1=p1,password_2=p2)
            messages.success(req, "Registration successful, please login")
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
                messages.error(req, "Email and password do not match")
                return redirect('login')
        else:
            messages.warning(req, "Email not registered, please sign up")
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
    







# ======================= ADMIN ============================================================ #

def admin_dashboard(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
        a_data = {
            "name": req.session['admin_name'],
            "email": req.session['admin_email'],
            "password": req.session['admin_password'],
        }

        # TEMPORARY COUNTS (dummy numbers)
        total_employees = Employee.objects.count()
        total_departments = Department.objects.count()
        total_queries = 20
        pending_queries = 5

        return render(req, 'admin_dashboard.html', {
            'data': a_data,
            'admin_dashboard': True,
            'total_employees': total_employees,
            'total_departments': total_departments,
            'total_queries': total_queries,
            'pending_queries': pending_queries,
        })

    # return render(req,"admin_dashboard.html")



def get_admin_data(req):
    if 'admin_email' in req.session:
        return {
            "name": req.session.get('admin_name'),
            "email": req.session.get('admin_email'),
            "password": req.session.get('admin_password'),
        }
    return None

def add_department(req):
    return render(req, "admin_dashboard.html", {
        "add_department": True,
        "data": get_admin_data(req)
    })

def save_department(req):
    if req.method == "POST":
        department_name = req.POST.get('department_name')
        department_code = req.POST.get('department_code')
        department_description = req.POST.get('department_description')
        department_head = req.POST.get('department_head')
        department_code_ck = Department.objects.filter(department_code=department_code)

        if not department_code_ck:
            Department.objects.create(
            department_name=department_name,
            department_code=department_code,
            department_description=department_description,   
            department_head=department_head)

            messages.success(req, "Department added successfully")
            return redirect("add_department")
        
        else:
            messages.error(req, "Department code already exists")
            return redirect("add_department")

    return render(req,'admin_dashboard.html')

def show_departments(req):
    departments = Department.objects.all()
    return render(req, "admin_dashboard.html", {
        "show_departments": True,
        "departments": departments,
        "data": get_admin_data(req)
    })

def add_employee(req):
    departments = Department.objects.all()
    return render(req, "admin_dashboard.html", {
        "add_employee": True,
        "departments": departments,
        "data": get_admin_data(req)
    })

def save_employee(req):
    if req.method == "POST":
        employee_id = req.POST.get('employee_id')
        name = req.POST.get('name')
        email = req.POST.get('email')
        dob = req.POST.get('dob')
        gender = req.POST.get('gender')
        department = req.POST.get('department')

        emp_id_ck = Employee.objects.filter(employee_id=employee_id)
        email_ck = Employee.objects.filter(email=email)

        if not emp_id_ck and not email_ck:
            Employee.objects.create(
                employee_id=employee_id,
                name=name,
                email=email,
                dob=dob,
                gender=gender,
                department=department
            )
            req.session['employee_password']=employee_id
            req.session['employee_email']=email

            subject = "Employee Account Created"
            message = f"""
                        Hello {name},

                        Your employee account has been created successfully.

                        Login Details:
                        Email    : {email}
                        Password : {employee_id}

                        Please keep these details safe.

                        Regards,
                        Admin Team
                        """

            send_mail(
                subject,
                message,
                "adityadas0217@gmail.com",
                [req.session.get('employee_email')],
                fail_silently=False,
            )
            messages.success(req, "Employee added successfully")
            return redirect("add_employee")

        else:
            # ❌ AUR YAHAN
            messages.error(req, "Employee ID or Email already exists")
            return redirect("add_employee")

    return redirect("add_employee")

def show_employees(req):
    employees = Employee.objects.all()
    return render(req, "admin_dashboard.html", {
        "show_employees": True,
        "employees": employees,
        "data": get_admin_data(req)
    })
