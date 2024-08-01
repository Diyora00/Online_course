from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Blog
from course.models import Course, Subject, Comment
from django.views import View
from course.forms import CommentForm, StudentModelForm
from django.contrib import messages

from django.views.generic import TemplateView
from django import forms
from course.models import Student
from teacher.models import Teacher


def index(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            if Student.objects.filter(user=request.user).exists():
                form.add_error(None, 'You have already signed up.')
            else:
                student.user = request.user
                student.save()

    subjects = Subject.objects.all().order_by('-id')[:4]
    teachers = Teacher.objects.all().order_by('-id')[:4]
    courses = Course.objects.all()[:3]
    blogs = Blog.objects.all().order_by('-id')[:4]
    context = {
        'form': form,
        'subjects': subjects,
        'teachers': teachers,
        'courses': courses,
        'blogs': blogs
    }

    return render(request, 'course/index.html', context)


class CourseListView(ListView):
    model = Course
    template_name = 'course/course.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context

    def get_queryset(self):
        queryset = Course.objects.all()
        subject_slug = self.kwargs.get('subject_slug')
        search_post = self.request.GET.get('search')
        if search_post:
            queryset = queryset.filter(title__icontains=search_post)
        if subject_slug:
            queryset = queryset.filter(subject__slug=subject_slug)
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = context['course'].teachers.all()
        comments = self.object.comments.all()
        context['comments'] = comments
        return context


class AddComment(TemplateView):
    template_name = 'course/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['form'] = form
        return context

    def post(self, request,  *args, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs.get('course_slug'))
        form = CommentForm(request.POST)
        context['form'] = form
        context['course'] = course
        messages.add_message(request, messages.SUCCESS, 'Your comment has been added.')

        comment = form.save(commit=False)
        comment.course = course
        comment.save()
        return redirect('course_detail', slug=course.slug)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
