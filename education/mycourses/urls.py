from django.urls import path
from .views import MyCoursesView

app_name = 'mycourses'

urlpatterns = [
    path('', MyCoursesView.as_view(), name='my_courses'),
]
