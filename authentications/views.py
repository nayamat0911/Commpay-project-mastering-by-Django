from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def login_profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('Invaled username or password')
            

    return render(request,'authentication/login.html')


def registration_profile(request):
    return render(request,'authentication/registation.html')


def forgot_password(request):
    return render(request,'authentication/forgot.html')