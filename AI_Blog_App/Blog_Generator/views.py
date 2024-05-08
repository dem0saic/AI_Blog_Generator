from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def usr_login(request):
    return render(request, 'login.html')


def usr_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Username already exists'
                return render(request,'signup.html', {'error_message': error_message})
        else:
            error_message = 'Password does not match'
            return render(request,'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')


def usr_logout(request):
    pass
