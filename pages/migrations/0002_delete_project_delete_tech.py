# Generated by Django 4.2.7 on 2023-11-09 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Tech',
        ),
    ]
