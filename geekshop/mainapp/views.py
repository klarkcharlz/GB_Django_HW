from django.shortcuts import render


# Create your views here.
def catalog(request):
    """Catalogs of books"""
    title = "Book of My Dreams: Каталог товаров."
    content = {'title': title}
    return render(request, "mainapp/catalogs.html", content)


def products(request, id):
    """books description"""
    books_title = {
        1: "Book of My Dreams: PostgreSQL. Основы языка SQL. Моргунов Е.П.",
        2: "Book of My Dreams: Микросервисы и контейнеры Docker. Парминдер С.К.",
        3: "Book of My Dreams: Разработка веб-приложений с использованием Flask на языке Python. Гринберг М.",
    }
    title = books_title[id]
    content = {'title': title}
    return render(request, f"mainapp/products/book_{id}.html", content)
