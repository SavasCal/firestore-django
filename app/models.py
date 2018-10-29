from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Color(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'color'

    def __unicode__(self):
        return self.nombre


class Local(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'local'

    def __unicode__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedor'

    def __unicode__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modelo'

    def __unicode__(self):
        return self.nombre


class Movimiento(models.Model):
    origen = models.ForeignKey('Local', models.DO_NOTHING, db_column='origen',related_name='origen', blank=True, null=True)
    destino = models.ForeignKey('Local', models.DO_NOTHING, db_column='destino', blank=True, null=True,related_name='movimiento')
    modelo = models.ForeignKey('Modelo', models.DO_NOTHING, db_column='modelo', blank=True, null=True,related_name='modelo')
    talla = models.ForeignKey('Talla', models.DO_NOTHING, db_column='talla', blank=True, null=True)
    color = models.ForeignKey('Color', models.DO_NOTHING, db_column='color', blank=True, null=True)
    cantidad = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=1000, blank=True, null=True)
    fecha = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movimiento'


class Talla(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'talla'

    def __unicode__(self):
        return self.nombre

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