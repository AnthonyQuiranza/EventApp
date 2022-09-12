# Generated by Django 4.1.1 on 2022-09-11 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_alter_session_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_end',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de inicio'),
            preserve_default=False,
        ),
    ]
