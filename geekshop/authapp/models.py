from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def basket_price(self):
        return sum(el.product_cost for el in self.basket.all())

    def basket_quantity(self):
        return sum(el.quantity for el in self.basket.all())
