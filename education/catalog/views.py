
import json
from django.shortcuts import render

def load_products():
    with open(r'D:\coursemarket\products.json', 'r') as file:
        data = json.load(file)
    return data


def catalog(request):
    products = load_products()
    context = {'products': products}
    return render(request, 'pages/catalog.html', context)

def catalog_detail(request, id):
    products = load_products()
    product = products.get(str(id))
    if product:
        context = {'product': product}
        return render(request, 'pages/catalog_detail.html', context)
    else:
        return render(request, 'pages/404.html')
