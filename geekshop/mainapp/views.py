from django.shortcuts import render

from .models import Book, Specifications, Author, Publisher, Translator
from basket.models import Basket


# Create your views here.
def catalog(request):
    basket = False
    total = Basket.get_price()
    cnt = Basket.get_count()
    if total and cnt:
        basket = True

    """Catalogs of books"""
    title = "Book of My Dreams: Каталог товаров."
    books = Book.objects.all()
    book_catal = []
    for book in books:
        book_catal.append({
            "name": book.name,
            "author": book.author,
            "image": book.image,
            "book_id": book.pk,
            "link": "products:book",
        })
    content = {'title': title, "books": book_catal, "basket": basket, "total": total, "cnt": cnt}
    return render(request, "mainapp/dynamic_catalog.html", content)


def products(request, id):
    """books description"""
    basket = False
    total = Basket.get_price()
    cnt = Basket.get_count()
    if total and cnt:
        basket = True

    book = Book.objects.get(pk=id)
    characteristics = {}
    images = book.image
    for key in book.__dict__:
        if book.__dict__[key]:
            characteristics[key] = book.__dict__[key]
    price = characteristics["price"]
    short_desc = characteristics["short_desc"]
    long_desc = characteristics["description"]
    title = f"{characteristics['name']}"

    characteristics["author_id"] = f"{Author.objects.get(pk=book.author_id).name} " \
                                   f"{Author.objects.get(pk=book.author_id).second_name}"
    characteristics["publisher_id"] = Publisher.objects.get(pk=book.publisher_id).name
    if "translator_id" in characteristics:
        characteristics["translator_id"] = f"{Translator.objects.get(pk=book.translator_id).name} " \
                                           f"{Translator.objects.get(pk=book.translator_id).second_name}"

    del characteristics["price"], characteristics["short_desc"], characteristics["description"], \
        characteristics["id"], characteristics["_state"], characteristics["image"], \
        characteristics["created_at"], characteristics["updated_at"]
    char = []
    for key in characteristics:
        char.append((Book._meta.get_field(key).verbose_name.title(), characteristics[key]))

    spec = Specifications.objects.get(for_book=id)
    specifications = {}
    for key in spec.__dict__:
        if spec.__dict__[key]:
            specifications[key] = spec.__dict__[key]
    del specifications["id"], specifications["_state"], specifications["for_book_id"], \
        specifications["created_at"], specifications["updated_at"]
    if "cover_type" in specifications:
        specifications["cover_type"] = dict(Specifications.cover)[specifications["cover_type"]]
    specifications["book_type"] = dict(Specifications.type)[specifications["book_type"]]
    tech_char = []
    for key in specifications:
        tech_char.append((Specifications._meta.get_field(key).verbose_name.title(), specifications[key]))

    content = {
        "price": price,
        "short_desc": short_desc,
        "long_desc": long_desc,
        "images": images,
        "title": title,
        "characteristics": char,
        "specifications": tech_char,
        "id": id,
        "basket": basket,
        "total": total,
        "cnt": cnt
    }
    print()
    return render(request, f"mainapp/products/dynamic_book.html", content)
