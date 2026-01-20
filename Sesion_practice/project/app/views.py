from django.shortcuts import render

# Create your views here.

# =============== COOKIES ============= #

# def  landing(req):
#     return render(req,'landing.html')

# def set(req):
#     if req.method=="POST":
#         n = req.POST.get('name')
#         e = req.POST.get('email')
#         p = req.POST.get('pass')
#         print(n,e,p)
#         response = render(req,'landing.html')
#         # response.set_cookie('name',n,max_age=60*60)
#         response.set_cookie('name',n)
#         response.set_cookie('email',e)
#         response.set_cookie('password',p)
#         return response
#     return render(req,'set.html')

# def get(req):
#     print(req.COOKIES)
#     c = req.COOKIES.get('csrftoken')
#     n = req.COOKIES['name']
#     e = req.COOKIES.get('email')
#     p = req.COOKIES.get('password')
#     t = req.COOKIES.get('Neeraj','Guest')
#     print(c,n,e,p,t)
#     return render(req,'get.html',{'name':n,'email':e,'pass':p,'demo':t})

# def delete(req):
#     return render(req,'delete.html')




# =============== SESSIONS ============= #

def  landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('pass')
        print(n,e,p)
        req.session['name'] = n
        req.session['email'] = e
        req.session['password'] = p
        print(req.session['name'],req.session['email'],req.session['password'])
        return render(req,'landing.html')
    
    return render(req,'set.html')



def  get(req):
    n = req.session['name']
    e = req.session['email']
    p = req.session['password']
    return render(req,'get.html', {'name':n,'email':e,'pass':p})

def  delete(req):
    req.session.flush()
    return render(req,'delete.html')