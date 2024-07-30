from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from teacher.models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teachers.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/teacher_detail.html'

