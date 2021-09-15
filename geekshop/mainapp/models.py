from django.db import models


# Create your models here.
class Author(models.Model):
    """Автор"""
    name = models.CharField(verbose_name='Имя', max_length=255)
    second_name = models.CharField(verbose_name='Фамилия', max_length=255)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.name} {self.second_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name", "second_name"]


class Translator(models.Model):
    """Переводчик"""
    name = models.CharField(verbose_name='Имя', max_length=255)
    second_name = models.CharField(verbose_name='Фамилия', max_length=255)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.name} {self.second_name}"

    class Meta:
        verbose_name = "Переводчик"
        verbose_name_plural = "Переводчики"
        ordering = ["name", "second_name"]


class Publisher(models.Model):
    """Издательство"""
    name = models.CharField(verbose_name='Наименование', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"
        ordering = ["name"]


class Book(models.Model):
    """Книга"""
    name = models.CharField(verbose_name='Наименование книги', max_length=255)
    image = models.ImageField(upload_to='book_images')
    short_desc = models.CharField(verbose_name='Краткое описание продукта', max_length=255)
    description = models.TextField(verbose_name='Полное описание продукта')
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Издательство")
    age_restrictions = models.CharField(verbose_name='Возрастной рейтинг', max_length=10)
    edition_language = models.CharField(verbose_name='Язык издания', max_length=50)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE, verbose_name="Переводчик",
                                   blank=True, null=True)
    year_of_issue = models.PositiveIntegerField(verbose_name="Год издания", blank=True, null=True)
    edition_type = models.CharField(max_length=255, verbose_name="Тип издания", blank=True)
    original_name = models.CharField(max_length=255, verbose_name="Название на оригинале", blank=True)
    ISBN = models.CharField(max_length=255, verbose_name="ISBN", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.name} - {self.author.name} {self.author.second_name}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["name", "author"]


class Specifications(models.Model):
    """Технические характеристики"""
    type = [
        ('Digital', 'Цифровая книга'),
        ('Printed', 'Печатная книга'),
    ]

    cover = [
        ('soft', 'Мягкая обложка'),
        ('hard', 'Твердая обложка'),
    ]

    for_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    package_weight = models.PositiveIntegerField(verbose_name='Вес в упаковке, г', blank=True, null=True)
    cover_type = models.CharField(verbose_name='Тип обложки', max_length=40, choices=cover, blank=True)
    edition_format = models.CharField(verbose_name='Формат издания', max_length=50, blank=True)
    number_of_pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    book_type = models.CharField(verbose_name='Тип издания', max_length=20, choices=type)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.for_book.name}-{self.book_type}"

    class Meta:
        verbose_name = "Технические характеристики книги"
        verbose_name_plural = "Технические характеристики книг"
        ordering = ["book_type"]
