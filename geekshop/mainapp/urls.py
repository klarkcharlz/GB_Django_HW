from django.urls import path

from .views import catalog, products

urlpatterns = [
    path("", catalog, name="catalog"),
    path("book/<int:id>/", products, name='book'),
]
