from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def logout_user(request):
    logout(request)
    return redirect('/home/')

def login_form(request):
    return render(request, 'login.html', {})

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home')
    return redirect(settings.LOGIN_URL, request)
