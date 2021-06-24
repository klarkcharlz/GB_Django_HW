from django.shortcuts import render


def index(request):
    """Main page"""
    title = "Book of My Dreams"
    content = {'title': title}
    return render(request, "geekshop/index.html", content)


def contacts(request):
    """Contacts page"""
    title = "Book of My Dreams: Контакты."
    content = {'title': title}
    return render(request, "geekshop/contacts.html", content)
