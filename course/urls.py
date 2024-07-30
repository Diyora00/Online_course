from django.urls import path
from course.views import *
from course.auth import *

urlpatterns = [
    path('', index, name='home'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('subject/<slug:subject_slug>/courses', CourseListView.as_view(), name='courses_of_subject'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('about/', about, name='about'),

    path('contact/', contact, name='contact'),
    path('course_detail/', course_details, name='course_details'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]

