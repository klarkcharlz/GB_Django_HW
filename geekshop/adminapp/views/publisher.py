from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Publisher
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import PublisherCreateForm


@user_passes_test(lambda u: u.is_superuser)
def publisher(request):
    title = 'админка/издательства'
    publisher_list = Publisher.objects.all()
    context = {
        'title': title,
        'objects': publisher_list
    }
    return render(request, 'adminapp/publisher/publisher.html', context)


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
    return render(request, 'adminapp/publisher/publisher_create.html', context)


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
    return render(request, 'adminapp/publisher/publisher_update.html', context)


def publisher_delete(request, pk):
    title = 'издательство/удалить'
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.is_deleted = True
        publisher.save()
        return HttpResponseRedirect(reverse('adminapp:publisher'))
    context = {'title': title, 'publisher_to_delete': publisher}
    return render(request, 'adminapp/publisher/publisher_delete.html', context)

