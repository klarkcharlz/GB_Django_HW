from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import ShopUser

from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def send_verify_email(user):
    verify_link = reverse('authnapp:verify', args=[user.email, user.activation_key])
    title = f'Активация на сайте, пользователя - {user.username}'
    message = f'Для активации вашей учетной {user.email} записи, напортале {settings.DOMAIN_NAME}' \
              f' перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            print("verification OK")
            return render(request, 'authnapp/verification.html')
        else:
            print(f'error activation user {user.username}')
            return render(request, 'authnapp/verification.html')
    except Exception as err:
        print(f"{type(err)}:\n{err}")
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('index'))


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
            user = register_form.save()
            if send_verify_email(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('authnapp:login'))
            else:
                print('ошибка отправки сообщения')
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
