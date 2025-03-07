# Generated by Django 5.1.6 on 2025-02-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Title')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('avaiable', models.BooleanField(default=True, verbose_name='Avaiable')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='User name')),
                ('email', models.EmailField(max_length=254, verbose_name='User e-mail')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='')),
            ],
        ),
    ]
