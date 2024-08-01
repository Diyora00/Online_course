from django.urls import path
from course.views import *
from course.auth import *
from root import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', index, name='home'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('subject/<slug:subject_slug>/courses', CourseListView.as_view(), name='courses_of_subject'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('about/', about, name='about'),
    path('course/<slug:course_slug>/detail/add_comment', AddComment.as_view(), name='comment'),

    path('contact/', contact, name='contact'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('verify-email-done/', verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

