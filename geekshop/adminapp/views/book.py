from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import UpdateView
from django.db import connection

from authnapp.views import db_profile_by_type
from mainapp.models import Book
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import BookCreateForm
from adminapp.forms import ProductCategoryEditForm


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


class ProductCategoryUpdateView(UpdateView):
    model = Book
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    form_class = ProductCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set. \
                    update(price=F('price') * (1 - discount / 100))
                db_profile_by_type(self.__class__, 'UPDATE', connection.queries)

        return super().form_valid(form)
