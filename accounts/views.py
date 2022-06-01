from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client

from .forms import ClientForm, CreatUserForm, UpdateUserForm

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
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect! (Contact admin if you think you are blocked)')
    context = {}
    return render(request,"accounts/login.html",context)

def userSignup(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cage = form.cleaned_data.get('age')
            # Cgender = request.POST.get('gender')
            client = Client.objects.create(
               user = user,
               age = Cage,
            #    gender = Cgender
            )
            messages.success(request, 'Account has been created for ' + user.first_name +" "+ user.last_name)
            greet = "Welcome to the MegaCart "+request.user.username
            messages.info(request, greet)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Couldn't create account. Please provide correct information!")

    context = {'form': form}
    return render(request,"accounts/signup.html",context)


def logoutView(request):
    logout(request)
    messages.info(request, "Hope to see you again!")
    return redirect("login")


def home(request):
    context = {}
    return render(request,"accounts/home.html",context)

def profile(request):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    userform = UpdateUserForm(instance=request.user)
    clientform = ClientForm(instance=client)
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        if userform.is_valid():
            print("hey")
            userform.save()
            messages.success(request, "Your Profile Information Has Been Updated!")
        else:
            messages.error(request, "There was an Issue While Updating Profile. Please Check If Your Information Is Valid!")
    context = {'userform': userform, 'clientform': clientform, 
    'user': user, 'albums': clientAlbums }
    return render(request,"accounts/profile.html",context)
    

def profileUpdate(request):
    user = request.user.client
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile Information Has Been Updated!")
        else:
            messages.error(request, "There was an Issue While Updating Profile. Please Check If Your Information Is Valid!")
                
    return redirect("profile")