# Generated by Django 4.1.1 on 2022-09-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_remove_session_speakers_session_speakers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='hour',
            field=models.TimeField(verbose_name='Hora'),
        ),
    ]
