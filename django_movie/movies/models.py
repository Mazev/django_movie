from datetime import date
from django.db import models
from django.urls import reverse


class Category(models.Model):
    # категория на филмите

    name = models.CharField(
        'Категория',
        max_length=150
    )

    description = models.TextField(
        'Описание'
    )

    url = models.SlugField(
        max_length=160
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    # Актьори и режисьори

    name = models.CharField(
        'Име',
        max_length=150
    )

    age = models.PositiveIntegerField(
        'Възраст',
        default=0
    )

    description = models.TextField(
        'Описание'
    )

    image = models.ImageField(
        'Изображение',
        upload_to='actors/'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акотьор и Режисьор'
        verbose_name_plural = 'Актьори и Режисьори'


class Genre(models.Model):
    # Жанрове
    name = models.CharField(
        'Име',
        max_length=100
    )

    description = models.TextField(
        'Описание'
    )

    url = models.SlugField(
        max_length=160,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанрове'


class Movie(models.Model):
    # Филми
    title = models.CharField(
        'Име',
        max_length=100
    )

    tagline = models.CharField(
        'Слоган',
        max_length=100,
        default=''
    )

    description = models.TextField(
        'Описание'
    )

    poster = models.ImageField(
        'Плакат',
        upload_to='movies/'
    )

    year = models.PositiveIntegerField(
        'Дата на премиера',
        default=2021
    )

    country = models.CharField(
        'Държава',
        max_length=50
    )

    directors = models.ManyToManyField(
        Actor,
        verbose_name='режисьор',
        related_name='film_director'
    )

    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актьор',
        related_name='film_actor'
    )

    genres = models.ManyToManyField(
        Genre,
        verbose_name='жанр'
    )

    world_premiere = models.DateField(
        'Световна премиера',
        default=date.today
    )

    budget = models.PositiveIntegerField(
        'Бюджет',
        default=0,
        help_text='бюджета е в долари'
    )

    fees_in_usa = models.PositiveIntegerField(
        'Приходи в САЩ',
        default=0,
        help_text='бюджета е в долари'
    )

    fees_in_world = models.PositiveIntegerField(
        'Приходи по цял свят',
        default=0,
        help_text='бюджета е в долари'
    )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )

    url = models.SlugField(
        max_length=160,
        unique=True
    )

    draft = models.BooleanField(
        'Чернова',
        default=False
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Филм'
        verbose_name_plural = 'Филми'


class MovieShot(models.Model):
    # Кадри от филма
    title = models.CharField(
        'Заглавие',
        max_length=100
    )

    description = models.TextField(
        'Описание'
    )

    image = models.ImageField(
        'Изображение',
        upload_to='movie_shots/'
    )

    movie = models.ForeignKey(
        Movie,
        verbose_name='Филм',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадър от филма'
        verbose_name_plural = 'Кадри от филми'


class Reviews(models.Model):
    # Коментари
    email = models.EmailField()
    name = models.CharField(
        'Име',
        max_length=100
    )

    text = models.TextField(
        'Съобщение',
        max_length=5000
    )

    movie = models.ForeignKey(
        Movie,
        verbose_name='филм',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментари'

