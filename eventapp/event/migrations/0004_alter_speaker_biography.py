# Generated by Django 4.1.1 on 2022-09-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='biography',
            field=models.TextField(max_length=400, verbose_name='Biografía o resumen'),
        ),
    ]
