from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Translator
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import TranslatorCreateForm


@user_passes_test(lambda u: u.is_superuser)
def translator(request):
    title = 'админка/переводчики'
    translator_list = Translator.objects.all()
    context = {
        'title': title,
        'objects': translator_list
    }
    return render(request, 'adminapp/translator/translator.html', context)


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
    return render(request, 'adminapp/translator/translator_create.html', context)


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
    return render(request, 'adminapp/translator/translator_update.html', context)


def translator_delete(request, pk):
    title = 'переводчик/удалить'
    translator = get_object_or_404(Translator, pk=pk)
    if request.method == 'POST':
        translator.is_deleted = True
        translator.save()
        return HttpResponseRedirect(reverse('adminapp:translator'))
    context = {'title': title, 'translator_to_delete': translator}
    return render(request, 'adminapp/translator/translator_delete.html', context)
