# Generated by Django 3.1.5 on 2021-04-24 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='room',
            new_name='rooms',
        ),
    ]