import json

from django.shortcuts import render, redirect
from django.conf import settings

from .models import PurchasedCourse


def my_courses(request):
    if request.user.is_authenticated:
        purchased_courses = PurchasedCourse.objects.filter(user=request.user)

        courses = []
        with open(r'D:\coursemarket\products.json', 'r') as file:
            all_courses = json.load(file)

        # Создаем список курсов для отображения
        for purchased_course in purchased_courses:
            course_id = str(purchased_course.course_id)
            course = all_courses.get(course_id)
            if course:
                courses.append(course)

        return render(request, 'pages/my_courses.html', {'courses': courses})

    return redirect('login:login')
