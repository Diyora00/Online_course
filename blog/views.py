from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

