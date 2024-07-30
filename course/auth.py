from django.shortcuts import render


def login(request):
    return render(request, 'auth/login.html')

def logout(request):
    return render(request, 'auth/logout.html')

def register(request):
    return render(request, 'auth/register.html')