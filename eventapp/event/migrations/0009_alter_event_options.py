# Generated by Django 4.1.1 on 2022-09-11 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_speaker_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
    ]