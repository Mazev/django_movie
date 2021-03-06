# Generated by Django 3.2.6 on 2021-08-21 11:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Име')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Възраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Акотьор и Режисьор',
                'verbose_name_plural': 'Актьори и Режисьори',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Име')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанрове',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Име')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Плакат')),
                ('year', models.PositiveIntegerField(default=2021, verbose_name='Дата на премиера')),
                ('country', models.CharField(max_length=50, verbose_name='Държава')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Световна премиера')),
                ('budget', models.PositiveIntegerField(default=0, help_text='бюджета е в долари', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='бюджета е в долари', verbose_name='Приходи в САЩ')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='бюджета е в долари', verbose_name='Приходи по цял свят')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чернова')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Актьор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='режисьор')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'Филм',
                'verbose_name_plural': 'Филми',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Име')),
                ('text', models.TextField(max_length=5000, verbose_name='Съобщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='филм')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментари',
            },
        ),
        migrations.CreateModel(
            name='MovieShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заглавие')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Филм')),
            ],
            options={
                'verbose_name': 'Кадър от филма',
                'verbose_name_plural': 'Кадри от филми',
            },
        ),
    ]
