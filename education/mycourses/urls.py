from django.urls import path

from .views import my_courses


app_name = 'mycourses'


urlpatterns = [
    path('', my_courses, name='usercourse'),
]
