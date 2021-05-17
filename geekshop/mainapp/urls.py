from django.urls import path

from .views import category
from .views import products

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:pk>/', category, name='category'),
]
