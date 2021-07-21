import random

from django.shortcuts import render

from mainapp.models import Book


def get_hot_product():
    products = Book.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Book.objects.all().exclude(pk=hot_product.pk)[0]
    return same_products


def index(request):
    """Main page"""
    title = "Book of My Dreams"
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {'title': title,
               "hot_product": hot_product,
               "same_products": same_products}
    return render(request, "geekshop/index.html", content)


def contacts(request):
    """Contacts page"""
    title = "Book of My Dreams: Контакты."
    content = {'title': title}
    return render(request, "geekshop/contacts.html", content)
