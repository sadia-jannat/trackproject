from django.shortcuts import render

# Create your views here
from django.http import HttpResponse
from django.contrib import admin
from apptrack import views

from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse,json
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#django signup and login
from django.contrib.auth.forms import UserCreationForm
from .forms import Create
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *

def companysignup(request):
     form=Create()
    
     if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
     context={'form':form}  
     return render(request,"company_signup.html",context)

login_result=1
def companylogin(request):
    
    if request.method == "POST":       
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            global login_result
            login_result=0
            
            login(request,user)

            return redirect('/search/') 

        else:
            messages.info(request,'Username and password incorrect')
    return render(request,"company_login.html")

def companylogout(request):
    logout(request)
    return redirect('/')

def employeeformfill(request):

    if request.method =="POST":
        em=Employee()

        em.name = request.POST.get('name')
        em.device_type = request.POST.get('device_type')
        em.device_name=request.POST.get('device_name')
        em.device_number = request.POST.get('device_number')
        em.given= request.POST.get('given')
        em.given_date=request.POST.get('given_date')
        em.returned = request.POST.get('returned')
        em.returned_date= request.POST.get('returned_date')

        em.save()

        messages.info(request,'Your data added successfully!!')
                    
    return render(request, "employeeform.html")

def devicelog(request):

    emp=Employee.objects.all()
    devicelist=Device.objects.all()

    lap=Employee.objects.filter(device_type='Laptop').count()
    lap=int(lap)
    
    tab=Employee.objects.filter(device_type='Tablets').count()
    tab=int(tab)
    
    mob=Employee.objects.filter(device_type='Mobile').count()
    mob=int(mob)

    ac_no = Employee.objects.filter(device_name='Acer').count()
    ac_no = int(ac_no)

    as_no = Employee.objects.filter(device_name='Asus').count()
    as_no = int(as_no)

    ap_no = Employee.objects.filter(device_name='Apple').count()
    ap_no = int(ap_no)

    handon=Employee.objects.filter(given='Yes').count()
    handon=int(handon)

    return_on=Employee.objects.filter(given='No').count()
    return_on=int(return_on)
   

    course_list = ['Acer', 'Asus']
    number_list = [as_no, ac_no]
    
    context={
        'devicelist':devicelist, 
        'emp':emp, 
        'course_list':course_list, 
        'number_list':number_list, 
        'lap':lap,
        'tab':tab,
        'mob':mob,

        'ac_no':ac_no,
        'as_no':as_no,
        'ap_no':ap_no,

        'handon':handon,
        'return_on':return_on,
        }
    return render(request, "devicelog.html", context)


def search(request):

    formfetch=Employee.objects.all() 
    products=Employee.objects.all()

    if request.method == 'GET':
        query = request.GET.get('query')   
        queryx=request.GET.get('queryx')
        queryday=request.GET.get('queryday')
        querydayx=request.GET.get('querydayx')

        if query and queryx and queryday:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontains=queryday).order_by('name')
        elif query and queryx or queryday:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontains=queryday).order_by('name')
        elif query or queryx and queryday:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontains=queryday).order_by('name')         
        elif query:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontain=queryday).order_by('name')
        elif queryx:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontain=queryday).order_by('name')
        elif queryday:
            products = Employee.objects.filter(device_type__icontains=query,device_name__icontains=queryx, device_number__icontain=queryday).order_by('name')                                
        else:
            print("No information to show")

    return render(request, 'search.html', {'products':products,'formfetch':formfetch})