# Generated by Django 4.1.1 on 2022-09-11 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_speaker_organization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Orador', 'verbose_name_plural': 'Oradores'},
        ),
    ]