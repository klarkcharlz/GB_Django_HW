import adminapp.views.author as author
import adminapp.views.translator as translator
import adminapp.views.book as book
import adminapp.views.user as user
import adminapp.views.specific as specific
import adminapp.views.publisher as publisher

from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.UserCreateView.as_view(), name='user_create'),
    path('users/read/', user.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UserDeleteView.as_view(), name='user_delete'),

    path('book/create/', book.book_create, name='book_create'),
    path('book/read/', book.book, name='book'),
    path('book/update/<int:pk>/', book.book_update, name='book_update'),
    path('book/delete/<int:pk>/', book.book_delete, name='book_delete'),

    path('specifications/create/', specific.specifications_create, name='specifications_create'),
    path('specifications/read/', specific.specifications, name='specifications'),
    path('specifications/update/<int:pk>/', specific.specifications_update, name='specifications_update'),
    path('specifications/delete/<int:pk>/', specific.specifications_delete, name='specifications_delete'),

    path('author/create/', author.author_create, name='author_create'),
    path('author/read/', author.author, name='author'),
    path('author/update/<int:pk>/', author.author_update, name='author_update'),
    path('author/delete/<int:pk>/', author.author_delete, name='author_delete'),

    path('translator/create/', translator.translator_create, name='translator_create'),
    path('translator/read/', translator.translator, name='translator'),
    path('translator/update/<int:pk>/', translator.translator_update, name='translator_update'),
    path('translator/delete/<int:pk>/', translator.translator_delete, name='translator_delete'),

    path('publisher/create/', publisher.publisher_create, name='publisher_create'),
    path('publisher/read/', publisher.publisher, name='publisher'),
    path('publisher/update/<int:pk>/', publisher.publisher_update, name='publisher_update'),
    path('publisher/delete/<int:pk>/', publisher.publisher_delete, name='publisher_delete'),

]
