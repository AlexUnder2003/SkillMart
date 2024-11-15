import json
from django.views.generic import TemplateView, View
from django.shortcuts import render


class ProductMixin:
    @staticmethod
    def load_products():
        with open(r'D:\coursemarket\products.json', 'r') as file:
            return json.load(file)


class CatalogView(ProductMixin, TemplateView):
    template_name = 'pages/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.load_products()
        return context


class CatalogDetailView(ProductMixin, View):
    def get(self, request, id, *args, **kwargs):
        products = self.load_products()
        product = products.get(str(id))

        if product:
            return render(request, 'pages/catalog_detail.html', {'product': product})
        return render(request, 'pages/404.html')
