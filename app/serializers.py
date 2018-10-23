from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers


class UsuariosSerializer(serializers.ModelSerializer):

	class Meta:
		model = Usuarios
		#fields = ('id', 'nombre','tipo_agente')
		fields = '__all__'


class HistorialGloboSerializer(serializers.ModelSerializer):

	class Meta:
		model = HistorialGlobo
		#fields = ('id', 'nombre','tipo_agente')
		fields = '__all__'
