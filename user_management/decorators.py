from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

#Often used for registration page,login page, in order to deny access registration page or login page who already have an account. 
def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func



