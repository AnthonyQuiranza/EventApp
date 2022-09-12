from operator import mod
from django.db import models

class Event(models.Model):
    name = models.CharField('Nombre',max_length=25)
    description = models.CharField('Descripción',max_length=200)
    icon = models.ImageField(upload_to='static/icons/')
    event_start = models.DateField('Fecha de inicio')
    event_end = models.DateField('Fecha de fin')
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class Speaker(models.Model):
    name = models.CharField('Nombre y Apellido', max_length=50)
    organization = models.CharField('Organización o cargo', max_length=100)
    biography = models.TextField('Biografía o resumen', max_length=400)
    photo = models.ImageField('Fotografía', upload_to='static/speakers/photo/')
    class Meta:
        verbose_name = 'Orador'
        verbose_name_plural = 'Oradores'
    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField('Nombre de la sesión', max_length=100)
    speakers = models.ManyToManyField(Speaker)
    description = models.TextField('Descripción de la sesión',max_length=400)
    date = models.DateField('Fecha')
    hour = models.TimeField('Hora')
    def nombre_speakers(self):
        return ",".join([str(p) for p in self.speakers.all()])
