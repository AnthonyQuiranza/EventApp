# Generated by Django 4.1.1 on 2022-09-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_speaker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='organization',
            field=models.CharField(max_length=100, verbose_name='Organización o cargo'),
        ),
    ]
