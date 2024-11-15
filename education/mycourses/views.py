import json
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import PurchasedCourse


class MyCoursesView(TemplateView):
    template_name = 'pages/my_courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            # Загружаем все курсы из JSON
            with open(r'D:\coursemarket\products.json', 'r') as file:
                all_courses = json.load(file)

            # Получаем приобретенные курсы пользователя
            purchased_courses = PurchasedCourse.objects.filter(user=self.request.user)
            courses = [
                all_courses.get(str(course.course))
                for course in purchased_courses
                if str(course.course) in all_courses
            ]

            context['courses'] = courses
        else:
            return redirect('login:login')

        return context
