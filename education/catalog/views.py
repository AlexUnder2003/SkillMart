
import json
from django.shortcuts import render

# Функция для загрузки данных из JSON
def load_products():
    with open(r'D:\coursemarket\products.json', 'r') as file:
        data = json.load(file)
    return data


# Отображение всего каталога
def catalog(request):
    products = load_products()
    context = {'products': products}
    return render(request, 'pages/catalog.html', context)

# Детальная страница продукта по ID
def catalog_detail(request, id):
    products = load_products()  # Загружаем продукты
    product = products.get(str(id))  # Используем строковый ключ для доступа
    if product:
        context = {'product': product}
        return render(request, 'pages/catalog_detail.html', context)
    else:
        return render(request, 'pages/404.html')  # В случае отсутствия продукта
