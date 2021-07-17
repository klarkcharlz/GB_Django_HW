from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    content = {'title': title,
               'login_form': login_form,
               'next': next,
               }
    return render(request, 'authnapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authnapp:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authnapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authnapp:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authnapp/edit.html', content)