# Generated by Django 4.2 on 2023-04-12 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='Users',
        ),
    ]
