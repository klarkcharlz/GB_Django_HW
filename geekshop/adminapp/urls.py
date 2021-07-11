import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('book/create/', adminapp.book_create, name='book_create'),
    path('book/read/', adminapp.book, name='book'),
    path('book/update/<int:pk>/', adminapp.book_update, name='book_update'),
    path('book/delete/<int:pk>/', adminapp.book_delete, name='book_delete'),

    path('specifications/create/', adminapp.specifications_create, name='specifications_create'),
    path('specifications/read/', adminapp.specifications, name='specifications'),
    path('specifications/update/<int:pk>/', adminapp.specifications_update, name='specifications_update'),
    path('specifications/delete/<int:pk>/', adminapp.specifications_delete, name='specifications_delete'),

    path('author/create/', adminapp.author_create, name='author_create'),
    path('author/read/', adminapp.author, name='author'),
    path('author/update/<int:pk>/', adminapp.author_update, name='author_update'),
    path('author/delete/<int:pk>/', adminapp.author_delete, name='author_delete'),

    path('translator/create/', adminapp.translator_create, name='translator_create'),
    path('translator/read/', adminapp.translator, name='translator'),
    path('translator/update/<int:pk>/', adminapp.translator_update, name='translator_update'),
    path('translator/delete/<int:pk>/', adminapp.translator_delete, name='translator_delete'),

    path('publisher/create/', adminapp.publisher_create, name='publisher_create'),
    path('publisher/read/', adminapp.publisher, name='publisher'),
    path('publisher/update/<int:pk>/', adminapp.publisher_update, name='publisher_update'),
    path('publisher/delete/<int:pk>/', adminapp.publisher_delete, name='publisher_delete'),

]
