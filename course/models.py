from django.db import models
from django.utils.text import slugify
from teacher.models import Teacher


class AbstractClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subject(AbstractClass):
    slug = models.SlugField(null=False, default='', unique=True, blank=True)
    title = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Course(AbstractClass):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, default='', unique=True, blank=True)
    number_of_students = models.PositiveIntegerField(default=0)
    description = models.TextField()
    price = models.FloatField()
    duration = models.PositiveIntegerField()
    teachers = models.ManyToManyField(Teacher, related_name='courses')
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    video = models.FileField(upload_to='media/videos')

    hours = models.PositiveIntegerField()
    minutes = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def duration_of_course(self):
        self.hours = self.duration // 60
        self.minutes = self.duration % 60
        return self.hours, self.minutes

    class Meta:
        ordering = ['-id']


class Comment(AbstractClass):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-id']
