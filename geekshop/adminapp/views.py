from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from adminapp.forms import ShopUserAdminEditForm
from authnapp.forms import ShopUserRegisterForm
from authnapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Book, Specifications, Author, Publisher, Translator
from django.contrib.auth.decorators import user_passes_test
from mainapp.forms import (BookCreateForm, SpecificationsCreateForm, TranslatorCreateForm, PublisherCreateForm,
                           AuthorCreateForm)
