# Generated by Django 4.1.1 on 2022-09-11 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Nombre de la sesión'),
            preserve_default=False,
        ),
    ]
