from django.db import models


class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'JUNIOR'
        MIDDLE = 'MIDDLE'
        SENIOR = 'SENIOR'

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    speciality = models.CharField(max_length=100)
    level = models.CharField(choices=LevelChoices, default=LevelChoices.JUNIOR.value, max_length=100)
    image = models.ImageField(upload_to='teachers_images/')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('course.Subject', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name
