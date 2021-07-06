from django.shortcuts import render

from basket.models import Basket


def index(request):
    """Main page"""
    basket = []
    total = 0
    cnt = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for prod in basket:
            total += prod.quantity * prod.product.price
            cnt += prod.quantity

    title = "Book of My Dreams"
    content = {'title': title, "basket": basket, "total": total, "cnt": cnt}
    return render(request, "geekshop/index.html", content)


def contacts(request):
    """Contacts page"""
    basket = []
    total = 0
    cnt = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for prod in basket:
            total += prod.quantity * prod.product.price
            cnt += prod.quantity

    title = "Book of My Dreams: Контакты."
    content = {'title': title, "basket": basket, "total": total, "cnt": cnt}
    return render(request, "geekshop/contacts.html", content)
