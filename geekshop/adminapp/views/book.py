from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Book
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import BookCreateForm


@user_passes_test(lambda u: u.is_superuser)
def book(request):
    title = 'админка/книги'
    book_list = Book.objects.all()
    context = {
        'title': title,
        'objects': book_list
    }
    return render(request, 'adminapp/book/book.html', context)


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
    return render(request, 'adminapp/book/book_create.html', context)


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
    return render(request, 'adminapp/book/book_update.html', context)


def book_delete(request, pk):
    title = 'книги/удаление'
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.is_deleted = True
        book.save()
        return HttpResponseRedirect(reverse('adminapp:book'))
    context = {'title': title, 'book_to_delete': book}
    return render(request, 'adminapp/book/book_delete.html', context)
