from django.shortcuts import render, redirect
from .models import Mydetails
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login, authenticate

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')   
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect(login)
    return render(request,'register.html')
    
def login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout(request):
    return redirect('login') 

def home(req):
    return render(req,'home.html')



def display(req):
    user = req.user 
    details = Mydetails.objects.filter(user=user)  
    return render(req, 'display.html', {'details': details})


def add(req):
    if req.method == 'POST':
        age = req.POST.get('age')
        phonenumber = req.POST.get('phonenumber')
        location = req.POST.get('location')
        file = req.FILES.get('file')  
        user = req.user     
        if age and phonenumber and location and file:  
            Mydetails.objects.create(user=user, age=age, phonenumber=phonenumber, location=location, file=file)
            return redirect('display')  
        else:
            return render(req, 'display.html', {'error': 'All fields are required.'})
    
    return render(req, 'display.html')


def edit(req, id):
    details = Mydetails.objects.get(pk=id)
    
    if req.method == 'POST':
        age = req.POST.get('age')
        phonenumber = req.POST.get('phonenumber')
        location = req.POST.get('location')
        file = req.FILES.get('file')        
        if age:
            details.age = age
        if phonenumber:
            details.phonenumber = phonenumber
        if location:
            details.location = location
        if file:
            details.file = file
        
        details.save()
        return redirect('view') 
    
    return render(req, 'edit.html', {'details': details})  

def delete(req, id):
    try:
        details = Mydetails.objects.get(pk=id)
        details.delete()
    except Mydetails.DoesNotExist:
        pass  
    
    return redirect('display') 