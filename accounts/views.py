from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            greet = "Welcome to the CL Dashboard "+request.user.username
            messages.info(request, greet)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is incorrect! (Contact admin if you think you are blocked)')
    context = {}
    return render(request,"accounts/login.html",context)

def userSignup(request):
    context = {}
    return render(request,"accounts/signup.html",context)