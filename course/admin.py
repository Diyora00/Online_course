from django.contrib import admin

from course.models import *

# Register your models here.
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)

