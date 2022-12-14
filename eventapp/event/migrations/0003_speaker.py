# Generated by Django 4.1.1 on 2022-09-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('organization', models.CharField(max_length=25, verbose_name='Organización o cargo')),
                ('biography', models.CharField(max_length=400, verbose_name='Biografía o resumen')),
                ('photo', models.FileField(upload_to='static/speakers/photo/', verbose_name='Fotografía')),
            ],
        ),
    ]
