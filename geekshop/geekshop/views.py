from django.shortcuts import render


def index(request):
    """Main page"""
    return render(request, "geekshop/index.html")


def contacts(request):
    """Contacts page"""
    return render(request, "geekshop/contacts.html")
