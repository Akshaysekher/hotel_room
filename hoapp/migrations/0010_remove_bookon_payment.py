# Generated by Django 3.1.5 on 2021-05-08 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoapp', '0009_bookon_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookon',
            name='payment',
        ),
    ]
