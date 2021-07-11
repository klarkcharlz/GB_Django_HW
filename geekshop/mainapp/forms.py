from django.forms import ModelForm
from .models import Book, Specifications, Translator, Publisher, Author


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class SpecificationsCreateForm(ModelForm):
    class Meta:
        model = Specifications
        fields = '__all__'


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class TranslatorCreateForm(ModelForm):
    class Meta:
        model = Translator
        fields = '__all__'


class PublisherCreateForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
