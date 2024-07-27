from django.urls import path
from teacher.views import teachers

urlpatterns = [
    path('teachers/', teachers, name='teachers')
]
