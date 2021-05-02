from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            uname = request.POST.get('username')
            pwd = request.POST.get('password')

            user = authenticate(request, username = uname, password = pwd)
            if user is not None:
                login(request, user)
                context = {'user':user}
                return render(request, 'home.html', context)
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('home')
