from django.http import HttpResponseRedirect
from django.shortcuts import render
from basketapp.models import Basket


# Create your views here.

def index(request):
    context = {}
    return render(request, 'basketapp/index.html', context)


def add(request, product_pk):
    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        product_id=product_pk,
    )
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    context = {}
    return render(request, 'basketapp/index.html', context)
