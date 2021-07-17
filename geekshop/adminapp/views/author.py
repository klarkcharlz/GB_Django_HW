from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Author
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import AuthorCreateForm


@user_passes_test(lambda u: u.is_superuser)
def author(request):
    title = 'админка/авторы'
    author_list = Author.objects.all()
    context = {
        'title': title,
        'objects': author_list
    }
    return render(request, 'adminapp/author/author.html', context)


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
    return render(request, 'adminapp/author/author_create.html', context)


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
    return render(request, 'adminapp/author/author_update.html', context)


def author_delete(request, pk):
    title = 'автор/удалить'
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.is_deleted = True
        author.save()
        return HttpResponseRedirect(reverse('adminapp:author'))
    context = {'title': title, 'author_to_delete': author}
    return render(request, 'adminapp/author/author_delete.html', context)
