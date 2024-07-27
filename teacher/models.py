from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    speciality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/teachers')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name
