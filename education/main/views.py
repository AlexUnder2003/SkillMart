from django.shortcuts import render


def index(request):
    """
    Отображает главную страницу
    """
    template = 'main/index.html'

    return render(request, template)

