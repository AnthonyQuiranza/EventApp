# Generated by Django 4.1.1 on 2022-09-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='icon',
            field=models.FileField(upload_to='static/icons/'),
        ),
    ]
