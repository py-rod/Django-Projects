# Generated by Django 4.2.1 on 2023-05-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]