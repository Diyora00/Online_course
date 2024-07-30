from django.views.generic import DetailView
from django.views.generic.list import ListView

from django.shortcuts import render
from course.models import Course, Subject


def index(request):
    return render(request, 'course/index.html')


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
        return context


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def course_details(request):
    return render(request, 'course/course_detail.html')

# class CourseList(ListView):
#     model = Course
