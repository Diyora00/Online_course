from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView

from course.forms import CommentForm
from blog.models import Blog
from django.contrib import messages
from django.views.generic import TemplateView


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = context['blog'].comments.all()


class AddComment(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['form'] = form
        return context

    def post(self, request,  *args, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = get_object_or_404(Blog, slug=self.kwargs.get('slug'))
        form = CommentForm(request.POST)
        context['form'] = form
        context['blog'] = blog

        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been added.')
        return redirect('blog_detail', slug=blog.slug)


def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            blog.comment = comment
            blog.save()

            return redirect('blog_detail', blog.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'form': form, 'blog': blog})