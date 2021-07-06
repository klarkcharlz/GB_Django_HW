from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .models import Basket
from mainapp.models import Book


def basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket
        }
        return render(request, 'basket/basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Book, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    return render(request, 'basket/basket.html')
