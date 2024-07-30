from django.urls import path
from blog.views import BlogDetailView, BlogListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<pk>', BlogDetailView.as_view(), name='blog_detail'),
]

