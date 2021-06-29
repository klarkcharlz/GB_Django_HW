from django.contrib import admin

from .models import Author, Translator, Publisher, Book, Specifications


# Register your models here.
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Specifications)
