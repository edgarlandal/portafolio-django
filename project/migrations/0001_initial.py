# Generated by Django 4.2.7 on 2023-11-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='projects_images/')),
                ('repository', models.URLField()),
                ('technologies', models.ManyToManyField(to='project.tech')),
            ],
        ),
    ]
