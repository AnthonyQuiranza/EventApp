# Generated by Django 4.1.1 on 2022-09-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_session_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='speakers',
        ),
        migrations.AddField(
            model_name='session',
            name='speakers',
            field=models.ManyToManyField(to='event.speaker'),
        ),
    ]