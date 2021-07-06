from django.shortcuts import render

from basket.models import Basket


def index(request):
    """Main page"""
    basket = False
    total = Basket.get_price()
    cnt = Basket.get_count()
    if total and cnt:
        basket = True

    title = "Book of My Dreams"
    content = {'title': title, "basket": basket, "total": total, "cnt": cnt}
    return render(request, "geekshop/index.html", content)


def contacts(request):
    """Contacts page"""
    basket = False
    total = Basket.get_price()
    cnt = Basket.get_count()
    if total and cnt:
        basket = True

    title = "Book of My Dreams: Контакты."
    content = {'title': title, "basket": basket, "total": total, "cnt": cnt}
    return render(request, "geekshop/contacts.html", content)
