from django.shortcuts import render


def index(request):
    return render(request, 'course/index.html')


def courses(request):
    return render(request, 'course/course.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
