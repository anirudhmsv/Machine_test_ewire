from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']    

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            print("Invalid Username or Password")
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')

    else:
        return render(request, 'login.html')
    


def home(request):
    return render(request, 'home.html')
