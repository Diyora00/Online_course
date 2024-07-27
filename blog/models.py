from django.db import models
from course.models import AbstractClass, Comment


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images')
    info = models.TextField()

    def __str__(self):
        return self.full_name


class Blog(AbstractClass):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(upload_to='media/blogs')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
