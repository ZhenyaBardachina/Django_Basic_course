from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def products(request):
    product_1 = Product.objects.all()[0]
    categories = ProductCategory.objects.all()

    context = {
        'page_title': 'каталог',
        'product_1': product_1,
        'categories': categories,
    }
    return render(request, 'products.html', context)


def category(request, pk):
    pass