from django.contrib.auth.hashers import make_password
from course.managers import CustomUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
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
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    video = models.FileField(upload_to='videos/')
    image = models.ImageField(upload_to='courses_images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def hour(self):
        if self.duration >= 60:
            hours = self.duration//60
            return hours

    @property
    def minute(self):
        if self.duration >= 60:
            minutes = self.duration % 60
            return minutes

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


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(unique=True, null=True, blank=True, max_length=50)
    phone_number = models.CharField(unique=True, null=True, blank=True, max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('-id',)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # this method must return what is assigned to USERNAME_FIELD (in this case 'email')
    # if anything else is returned it arises an ERROR
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @property
    def split_email(self):
        return self.email.split('@')[0]


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
