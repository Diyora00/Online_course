from django.urls import path
from teacher.views import *

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teacher_detail/<pk>/', TeacherDetailView.as_view(), name='teacher_detail')
]
