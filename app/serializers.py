from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers



class ModeloSerializer(serializers.ModelSerializer):

	class Meta:
		model = Modelo
		fields = '__all__'


class MovimientoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movimiento
		fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):

	

	class Meta:
		model = Local
		fields = '__all__'


