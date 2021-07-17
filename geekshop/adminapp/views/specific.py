from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Specifications
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import SpecificationsCreateForm


@user_passes_test(lambda u: u.is_superuser)
def specifications(request):
    title = 'книги/технические характеристики книг'
    specification_list = Specifications.objects.all()
    context = {
        'title': title,
        'objects': specification_list
    }
    return render(request, 'adminapp/specifications/specifications.html', context)


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
    return render(request, 'adminapp/specifications/specifications_create.html', context)


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
    return render(request, 'adminapp/specifications/specifications_update.html', context)


def specifications_delete(request, pk):
    title = 'книги/удалить технические характеристики'
    spec = get_object_or_404(Specifications, pk=pk)
    if request.method == 'POST':
        spec.is_deleted = True
        spec.save()
        return HttpResponseRedirect(reverse('adminapp:specifications'))
    context = {'title': title, 'spec_to_delete': spec}
    return render(request, 'adminapp/specifications/specifications_delete.html', context)
