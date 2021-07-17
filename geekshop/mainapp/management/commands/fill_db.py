import json
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from ....mainapp.models import Author, Publisher, Translator, Book, Specifications

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    @staticmethod
    def handle(*args, **options):
        Specifications.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        Translator.objects.all().delete()
        Publisher.objects.all().delete()

        authors = load_from_json('authors')
        for author in authors:
            new_author = Author(**author)
            new_author.save()

        translators = load_from_json('translators')
        for translator in translators:
            new_translator = Author(**translator)
            new_translator.save()

        publishers = load_from_json('publishers')
        for publisher in publishers:
            new_publisher = Author(**publisher)
            new_publisher.save()

        books = load_from_json('books')
        for book in books:
            author = book["author"]
            publisher = book["publisher"]
            translator = book["translator"]
            _author = Author.objects.get(name=author)
            book['author'] = _author
            _publisher = Publisher.objects.get(name=publisher)
            book['publisher'] = _publisher
            _translator = Translator.objects.get(name=translator)
            book['translator'] = _translator
            new_book = Book(**book)
            new_book.save()

        specifications = load_from_json('specifications')
        for specification in specifications:
            book = specification["for_book"]
            _book = Book.objects.get(name=book)
            specification['for_book'] = _book
            new_specification = Specifications(**specification)
            new_specification.save()

        # Создаем суперпользователя при помощи менеджера модели
        User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')
