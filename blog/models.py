from django.db import models
from course.models import AbstractClass, Comment


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/')
    info = models.TextField()

    def __str__(self):
        return self.full_name


class Blog(AbstractClass):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ManyToManyField(Author, related_name='blogs')
    image = models.ImageField(upload_to='blogs_images/')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
