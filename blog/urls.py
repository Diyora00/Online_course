from django.urls import path
from blog.views import BlogDetailView, BlogListView, AddComment

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_detail/<slug:slug>/add_comment/', AddComment.as_view(), name='comment_blog'),
]
