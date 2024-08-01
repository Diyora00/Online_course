from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/')
    info = models.TextField()

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, default='', unique=True, blank=True)
    body = models.TextField()
    author = models.ManyToManyField(Author, related_name='blogs')
    image = models.ImageField(upload_to='blogs_images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
