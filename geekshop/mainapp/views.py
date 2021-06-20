from django.shortcuts import render


# Create your views here.
def catalog(request):
    return render(request, "mainapp/catalogs.html")


def products(request, id):
    return render(request, f"mainapp/products/book_{id}.html")
