from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from authnapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users/users.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/users/user_create.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['title'] = 'пользователи/создать'
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/users/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи/редактировать'
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/users/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи/удаление'
        return context
