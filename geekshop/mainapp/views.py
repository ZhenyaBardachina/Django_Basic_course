from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def get_menu():
    return ProductCategory.objects.all()


def products(request):
    product_1 = Product.objects.all()[0]

    context = {
        'page_title': 'каталог',
        'product_1': product_1,
        'categories': get_menu(),
    }
    return render(request, 'products.html', context)


def category(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all()
            category = {'pk': 0, 'name': 'все', }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            # products = category.product_set.all()
            products = Product.objects.filter(category__pk=pk)

    context = {
        'page_title': 'товары категории',
        'categories': get_menu(),
        'category': category,
        'products': products,
        'basket': basket,
    }

    return render(request, 'category_products.html', context)






