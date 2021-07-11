from django.http import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm
from authnapp.forms import ShopUserRegisterForm
from authnapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Book, Specifications, Author, Publisher, Translator
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import (BookCreateForm, SpecificationsCreateForm,
                            TranslatorCreateForm, PublisherCreateForm,
                            AuthorCreateForm)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    context = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'пользователи/создать'
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserRegisterForm()
    context = {
        'title': title,
        'user_form': user_form
    }
    return render(request, 'adminapp/user_create.html', context)


def user_update(request, pk):
    title = 'пользователи/редактировать'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)
    context = {
        'title': title,
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'пользователи/удаление'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_deleted = True
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))
    context = {'title': title, 'user_to_delete': user}
    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def book(request):
    title = 'админка/книги'
    book_list = Book.objects.all()
    context = {
        'title': title,
        'objects': book_list
    }
    return render(request, 'adminapp/book.html', context)


def book_create(request):
    title = 'книги/создать'
    if request.method == 'POST':
        book_form = BookCreateForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse('adminapp:book'))
    else:
        book_form = BookCreateForm()
    context = {
        'title': title,
        'book_form': book_form
    }
    return render(request, 'adminapp/book_create.html', context)


def book_update(request, pk):
    title = 'книги/редактировать'
    edit_book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book_form = BookCreateForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse('adminapp:book_update', args=[edit_book.pk]))
    else:
        book_form = BookCreateForm(instance=edit_book)
    context = {
        'title': title,
        'book_form': book_form,
    }
    return render(request, 'adminapp/book_update.html', context)


def book_delete(request, pk):
    title = 'книги/удаление'
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.is_deleted = True
        book.save()
        return HttpResponseRedirect(reverse('adminapp:book'))
    context = {'title': title, 'book_to_delete': book}
    return render(request, 'adminapp/book_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def specifications(request):
    title = 'книги/технические характеристики книг'
    specification_list = Specifications.objects.all()
    context = {
        'title': title,
        'objects': specification_list
    }
    return render(request, 'adminapp/specifications.html', context)


def specifications_create(request):
    title = 'книги/заполнить технические характеристики'
    if request.method == 'POST':
        specifications_form = SpecificationsCreateForm(request.POST, request.FILES)
        if specifications_form.is_valid():
            specifications_form.save()
            return HttpResponseRedirect(reverse('adminapp:specifications'))
    else:
        specifications_form = SpecificationsCreateForm()
    context = {
        'title': title,
        'specifications_form': specifications_form
    }
    return render(request, 'adminapp/specifications_create.html', context)


def specifications_update(request, pk):
    title = 'книги/редактировать технические характеристики'
    edit_spec = get_object_or_404(Specifications, pk=pk)
    if request.method == 'POST':
        spec_form = SpecificationsCreateForm(request.POST, request.FILES)
        if spec_form.is_valid():
            spec_form.save()
            return HttpResponseRedirect(reverse('adminapp:specifications_update', args=[edit_spec.pk]))
    else:
        spec_form = SpecificationsCreateForm(instance=edit_spec)
    context = {
        'title': title,
        'spec_form': spec_form,
    }
    return render(request, 'adminapp/specifications_update.html', context)


def specifications_delete(request, pk):
    title = 'книги/удалить технические характеристики'
    spec = get_object_or_404(Specifications, pk=pk)
    if request.method == 'POST':
        spec.is_deleted = True
        spec.save()
        return HttpResponseRedirect(reverse('adminapp:specifications'))
    context = {'title': title, 'spec_to_delete': spec}
    return render(request, 'adminapp/specifications_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def author(request):
    title = 'админка/авторы'
    author_list = Author.objects.all()
    context = {
        'title': title,
        'objects': author_list
    }
    return render(request, 'adminapp/author.html', context)


def author_create(request):
    title = 'автор/создать'
    if request.method == 'POST':
        author_form = AuthorCreateForm(request.POST, request.FILES)
        if author_form.is_valid():
            author_form.save()
            return HttpResponseRedirect(reverse('adminapp:author'))
    else:
        author_form = AuthorCreateForm()
    context = {
        'title': title,
        'author_form': author_form
    }
    return render(request, 'adminapp/author_create.html', context)


def author_update(request, pk):
    title = 'автор/редактировать'
    edit_author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author_form = AuthorCreateForm(request.POST, request.FILES)
        if author_form.is_valid():
            author_form.save()
            return HttpResponseRedirect(reverse('adminapp:author_update', args=[edit_author.pk]))
    else:
        author_form = AuthorCreateForm(instance=edit_author)
    context = {
        'title': title,
        'author_form': author_form,
    }
    return render(request, 'adminapp/author_update.html', context)


def author_delete(request, pk):
    title = 'автор/удалить'
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.is_deleted = True
        author.save()
        return HttpResponseRedirect(reverse('adminapp:author'))
    context = {'title': title, 'author_to_delete': author}
    return render(request, 'adminapp/author_delete.html', context)


def translator(request):
    title = 'админка/переводчики'
    translator_list = Translator.objects.all()
    context = {
        'title': title,
        'objects': translator_list
    }
    return render(request, 'adminapp/translator.html', context)


def translator_create(request):
    title = 'переводчик/создать'
    if request.method == 'POST':
        translator_form = TranslatorCreateForm(request.POST, request.FILES)
        if translator_form.is_valid():
            translator_form.save()
            return TranslatorCreateForm(reverse('adminapp:translator'))
    else:
        translator_form = TranslatorCreateForm()
    context = {
        'title': title,
        'translator_form': translator_form
    }
    return render(request, 'adminapp/translator_create.html', context)


def translator_update(request, pk):
    title = 'переводчик/редактировать'
    edit_translator = get_object_or_404(Translator, pk=pk)
    if request.method == 'POST':
        translator_form = TranslatorCreateForm(request.POST, request.FILES)
        if translator_form.is_valid():
            translator_form.save()
            return HttpResponseRedirect(reverse('adminapp:translator_update', args=[edit_translator.pk]))
    else:
        translator_form = TranslatorCreateForm(instance=edit_translator)
    context = {
        'title': title,
        'translator_form': translator_form,
    }
    return render(request, 'adminapp/translator_update.html', context)


def translator_delete(request, pk):
    title = 'переводчик/удалить'
    translator = get_object_or_404(Translator, pk=pk)
    if request.method == 'POST':
        translator.is_deleted = True
        translator.save()
        return HttpResponseRedirect(reverse('adminapp:translator'))
    context = {'title': title, 'translator_to_delete': translator}
    return render(request, 'adminapp/translator_delete.html', context)


def publisher(request):
    title = 'админка/издательства'
    publisher_list = Publisher.objects.all()
    context = {
        'title': title,
        'objects': publisher_list
    }
    return render(request, 'adminapp/publisher.html', context)


def publisher_create(request):
    title = 'издательство/создать'
    if request.method == 'POST':
        publisher_form = PublisherCreateForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponseRedirect(reverse('adminapp:publisher'))
    else:
        publisher_form = PublisherCreateForm()
    context = {
        'title': title,
        'publisher_form': publisher_form
    }
    return render(request, 'adminapp/publisher_create.html', context)


def publisher_update(request, pk):
    title = 'издательство/редактировать'
    edit_publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher_form = PublisherCreateForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponseRedirect(reverse('adminapp:publisher_update', args=[edit_publisher.pk]))
    else:
        publisher_form = PublisherCreateForm(instance=edit_publisher)
    context = {
        'title': title,
        'publisher_form': publisher_form,
    }
    return render(request, 'adminapp/publisher_update.html', context)


def publisher_delete(request, pk):
    title = 'издательство/удалить'
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.is_deleted = True
        publisher.save()
        return HttpResponseRedirect(reverse('adminapp:publisher'))
    context = {'title': title, 'publisher_to_delete': publisher}
    return render(request, 'adminapp/publisher_delete.html', context)

