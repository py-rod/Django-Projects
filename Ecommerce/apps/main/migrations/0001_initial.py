# Generated by Django 4.2.1 on 2023-05-11 22:25

import apps.main.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='./Default/noimage.png', max_length=255, upload_to=apps.main.models.Carousel.image_upload_to)),
                ('image2', models.ImageField(default='./Default/noimage.png', max_length=255, upload_to=apps.main.models.Carousel.image_upload_to)),
                ('image3', models.ImageField(default='./Default/noimage.png', max_length=255, upload_to=apps.main.models.Carousel.image_upload_to)),
            ],
            options={
                'verbose_name_plural': 'Carousel',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='./Default/noproduct.jpg', max_length=255, upload_to=apps.main.models.Products.image_upload_to)),
                ('taxes', models.CharField(choices=[('Include', 'Include'), ('Not included', 'Not included')], default='', max_length=100)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField(default='', max_length=700)),
                ('product_slug', models.SlugField(unique=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('series', models.ForeignKey(default='', help_text='Select the categorie of the product', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.categories')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'Products',
                'ordering': ('-id',),
            },
        ),
    ]