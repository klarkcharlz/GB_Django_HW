from django.db import models
from django.conf import settings
from mainapp.models import Book


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @classmethod
    def get_price(cls):
        total = 0
        for prod in cls.objects.all():
            total += prod.quantity * prod.product.price
        return total

    @classmethod
    def get_count(cls):
        cnt = 0
        for prod in cls.objects.all():
            cnt += prod.quantity
        return cnt
