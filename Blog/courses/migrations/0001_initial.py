# Generated by Django 4.2 on 2023-04-12 23:12

import colorfield.fields
import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('bg_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='Select color for background image', image_field=None, max_length=18, samples=None, verbose_name='Choise Color')),
                ('image', models.ImageField(default='./default/noimage_curso.png', max_length=255, upload_to=courses.models.Courses.image_upload_to)),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'db_table': 'Couses',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ArticleCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.CharField(blank=True, default='', max_length=600, verbose_name='Description')),
                ('image', models.ImageField(default='./default/noimage_curso.png', max_length=255, upload_to=courses.models.ArticleCourse.image_upload_to)),
                ('article_slug', models.SlugField(default='', unique=True, verbose_name='Article Slug')),
                ('content', tinymce.models.HTMLField(blank=True, default='')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Modified')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('series', models.ForeignKey(default='', help_text='Select course for create article', on_delete=django.db.models.deletion.SET_DEFAULT, to='courses.courses')),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'db_table': 'Articles',
                'ordering': ('-id',),
            },
        ),
    ]