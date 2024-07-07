from django.shortcuts import render, redirect
from jobPortalApp.models import *
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from jobPortalApp.newforms import *

def createUser(request):
    if request.method == 'POST':
        userform = CreateUserForm(request.POST, request.FILES)
        if userform.is_valid():
            userform.save()
            return redirect('loginpage')
    else:
        userform = CreateUserForm()
    context = {
        'userform':userform
    }
    
    return render(request,'formtemplate/createuser.html',context)

def loginpage(request):
    
    if request.method == 'POST':
        userform = UserLoginForm(request,request.POST)
        if userform.is_valid():
            user=userform.get_user()
            login(request,user)
            return redirect('createUser')
    else:
        userform = UserLoginForm()
    context = {
        'userform':userform
    }
    
    return render(request,'formtemplate/login.html',context)