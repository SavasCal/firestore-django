from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'estado'
        verbose_name = 'Estado'

    def __unicode__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'globo'
        verbose_name = 'Usuario'

    def __unicode__(self):
        return self.nombre



class HistorialGlobo(models.Model):
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.today())
    fecha_inicio = models.DateTimeField(blank=True, default=datetime.datetime.today())
    fecha_fin = models.DateTimeField(blank=True, default=datetime.datetime.today())


    class Meta:
        managed = True
        db_table = 'historial_globo'
        verbose_name = 'Historial Globo'

    def __unicode__(self):
        return self.usuario