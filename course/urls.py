from django.urls import path
from course.views import index, courses, about, contact

urlpatterns = [
    path('', index, name='home'),
    path('courses/', courses, name='courses'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
