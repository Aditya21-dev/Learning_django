from django.shortcuts import render, redirect
from .models import User, Department , Employee , Query
from .models import Employee, Department
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
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
        
        employee = Employee.objects.filter(email=e, employee_id=p).first()
        if employee:
            req.session['employee_email'] = employee.email
            req.session['employee_name'] = employee.name
            return redirect('employee_dashboard')
        
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
        total_employees = Employee.objects.count()
        total_departments = Department.objects.count()
        total_queries = Query.objects.count()
        pending_queries = Query.objects.filter(status='Pending').count()

        return render(req, 'admin_dashboard.html', {
            'data': a_data,
            'admin_dashboard': True,
            'total_employees': total_employees,
            'total_departments': total_departments,
            'total_queries': total_queries,
            'pending_queries': pending_queries,
        })
    
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
    
@never_cache
def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')
    
    if 'employee_email' in req.session:
        req.session.flush()
        return redirect('login')
    
    if 'admin_email' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')
    












# ======================= ADMIN ============================================================ #

@never_cache
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
        total_queries = Query.objects.count()
        pending_queries = Query.objects.filter(status='Pending').count()

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
            req.session['employee_name']=name

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

def show_queries(req):
    employees_queries = Query.objects.all()
    return render(req, "admin_dashboard.html", {
        "show_queries": True,
        "employee_queries": employees_queries,
        "data": get_admin_data(req)
    })

def reply_quer(req,q_id):
    query = Query.objects.get(id = q_id)

    if req.method == 'POST':
        admin_reply = req.POST.get("admin_reply")
        query.admin_reply = admin_reply
        query.status = "Resolved"
        query.save()
        return redirect("show_queries")
    
    return render(req, "admin_dashboard.html", {
        "reply_form": True,
        "q": query,
        "data": get_admin_data(req)
    })














# ===================== EMPLOYEE DASHBOARD =================== #

@never_cache
def employee_dashboard(req):
    email = req.session.get('employee_email')
    if not email:
        return redirect('login')
    a_data = req.session.get('employee_name')
    employee = Employee.objects.filter(email=email).first()

    return render(req, 'employee_dashboard.html', { 
        "employee_dashboard":True,
        'employee': employee,
        'data':{'name':a_data}
    })


def Queries(req):
    a_data = {"name": req.session.get('employee_name')}
    return render(req,'employee_dashboard.html',{"Queries":True,'data':a_data,})

def raise_query(req):
    email = req.session.get('employee_email')
    
    employee_data = Employee.objects.filter(email=email).first()
    a_data = {"name": req.session.get('employee_name')}
    if employee_data:
        return render(req, 'employee_dashboard.html', {
            "raise_query": True,
            "employee_data":employee_data,
            'data':a_data,
    })


def save_query(req):
    if req.method == "POST":
        name = req.POST.get('name')
        email = req.POST.get('email')
        department = req.POST.get('department')
        query = req.POST.get('query')

        Query.objects.create(
            name=name,
            email=email,
            department=department,
            query=query
        )
        messages.success(req, "Querry send successfully....! ")
        return redirect('Queries')   
    return redirect('Queries') 
    
def total_queries(req):
    email = req.session.get('employee_email')
    employee_queries = Query.objects.filter(email=email)
    a_data = {"name": req.session.get('employee_name')}
    return render(req, 'employee_dashboard.html', {
        "total_queries": True,
        "employee_queries":employee_queries,
        'data':a_data,
    })

def solved_queries(req):
    email = req.session.get('employee_email')
    employee_queries = Query.objects.filter(email=email,status="Resolved")
    a_data = {"name": req.session.get('employee_name')}
    return render(req, 'employee_dashboard.html', {
        "solved_queries": True,
        "employee_queries":employee_queries,
        'data':a_data,
    })

def pending_queries(req):
    email = req.session.get('employee_email')
    employee_queries = Query.objects.filter(email=email,status="Pending")
    a_data = {"name": req.session.get('employee_name')}
    return render(req, 'employee_dashboard.html', {
        "pending_queries": True,
        "employee_queries":employee_queries,
        'data':a_data,
    })

def edit_query(req,q_id):
    query = Query.objects.get(id = q_id)
    a_data = {"name": req.session.get('employee_name')}
    return render(req, "employee_dashboard.html", {
        "edit_queryform": True,
        "q": query,
        'data':a_data,
    })

def update_query(req,q_id):
    if req.method == "POST":
        query = Query.objects.get(id = q_id)
        query.query = req.POST.get('query')
        query.save()
        return redirect('pending_queries')

def delete_query(req,q_id):
    query = Query.objects.get(id=q_id)
    query.delete()
    return redirect("pending_queries")