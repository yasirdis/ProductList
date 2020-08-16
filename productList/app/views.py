from django.shortcuts import render,redirect
from app.models import Product, UserDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
message=""

@login_required(login_url='loginPage')
def index(request):
    allproducts =Product.objects.all()
    return render(request,'index.html',context={"ProductList":allproducts,"usrname":request.session['usrname']})

@login_required(login_url='loginPage')
def ProDetail(request):
    data = request.GET.get('data')
    product = Product.objects.get(Id=data)
    return render(request,'ProductDetail.html',context={"product":product})

def validiateUser(request):
    data=request.GET.get('data')
    print(data)
    type=request.GET.get('type')
    print(type)
    if type =='email':
        result = validatebyemail(data)
    else:
        result = validatebyUN(data)
        print(result)
    return JsonResponse({"result":result})

def validatebyUN(data):
    try:
        usename= User.objects.get(username=data)
        return "Username Aleady exists"
    except User.DoesNotExist:
        return "OK"

def validatebyemail(data):
    try:
        email= User.objects.get(email=data)
        return "email Aleady exists"
    except User.DoesNotExist:
        return "OK"

def registerUser(request):
    username=request.POST.get('un')
    email=request.POST.get('email')
    password=request.POST.get('password')
    fn = request.POST.get('fn')
    ln = request.POST.get('ln')
    ph = request.POST.get('ph')
    user = User.objects.create_user(username,email,password)
    user.last_name = ln
    user.first_name = fn
    user.save()
    usrphone = UserDetails(user=user,Phone=ph)
    usrphone.save()
    global message
    message="User Registration Successfull"
    return redirect('registrationPage')

def registrationPage(request):
    global message
    msg = message
    message=""
    return render(request,'Registration.html',context={"message":msg})

def loginPage(request):
    global message
    msg = message
    message=""
    return render(request,'Login.html',context={"message":msg})

def userAuth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['usrname'] = username
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    else:
        global message
        message="username or password incorrect"
    return redirect('/')

@login_required(login_url='loginPage')
def logout_view(request):
    del request.session['usrname']
    logout(request)
    return redirect('loginPage')
