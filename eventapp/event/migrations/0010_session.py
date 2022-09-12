# Generated by Django 4.1.1 on 2022-09-11 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_alter_event_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=400, verbose_name='Descripción de la sesión')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('hour', models.DateTimeField(verbose_name='Hora')),
                ('speakers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.speaker')),
            ],
        ),
    ]
