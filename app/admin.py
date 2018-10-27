#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter

@admin.register(Color)
class ColorGloboAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Talla)
class TallaGloboAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Movimiento)
class MovimientoGloboAdmin(admin.ModelAdmin):
    list_display = ('id','origen')

@admin.register(Local)
class LocalGloboAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(Modelo)
class ModeloGloboAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')