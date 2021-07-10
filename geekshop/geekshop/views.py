import random

from django.shortcuts import render

from basket.models import Basket
from mainapp.models import Book


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Book.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Book.objects.all().exclude(pk=hot_product.pk)[0]
    return same_products


def index(request):
    """Main page"""
    title = "Book of My Dreams"

    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {'title': title,
               "basket": basket,
               "hot_product": hot_product,
               "same_products": same_products}
    return render(request, "geekshop/index.html", content)


def contacts(request):
    """Contacts page"""
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = "Book of My Dreams: Контакты."
    content = {'title': title, "basket": basket}
    return render(request, "geekshop/contacts.html", content)



