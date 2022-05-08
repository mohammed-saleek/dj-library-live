from multiprocessing import AuthenticationError, context
import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#User Registration
def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registration Successful')
            return redirect('/')
        messages.error(request, "Registration Unsuccessful. Invalid Data")
    form = NewUserForm()
    context = {'register_form':form}
    return render(request,'user_management/registration.html',context)

#User Login function
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid Credentials!!!")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'user_management/login.html',context)

#User Logout function
def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully Logged Out.")
    return redirect('/user/login/')