from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse,JsonResponse
from app.serializers import *

import firebase_admin
from firebase_admin import credentials,firestore
import string
import random
import datetime as dt


# Create your views here.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    
	print('ksksk')


def guarda(request):

	# cred = credentials.Certificate("clave.json")

	# firebase_admin.initialize_app(cred, {
	#     'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
	# })

	# db=firestore.client()

	# loc = db.collection(u'locales').get()

	# Local.objects.all().delete()

	# for lo in loc:

	# 	loca = lo.to_dict()['nombre']

	# 	Local(nombre=loca).save()

	# loc = db.collection(u'modelos').get()

	# for lo in loc:

	# 	loca = lo.to_dict()['nombre']

	# 	Modelo(nombre=loca).save()

	# loc = db.collection(u'talla').get()

	# for lo in loc:

	# 	loca = lo.to_dict()['nombre']

	# 	Talla(nombre=loca).save()


	# loc = db.collection(u'colores').get()

	# for lo in loc:

	# 	loca = lo.to_dict()['nombre']

	# 	Color(nombre=loca).save()

	loc = db.collection(u'colores').get()

	for lo in loc:

		loca = lo.to_dict()['nombre']

		Color(nombre=loca).save()


	

	return HttpResponse('data', content_type="application/json")


def listausuarios(request):


	cred = credentials.Certificate("clave.json")

	firebase_admin.initialize_app(cred, {
	    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
	})

	db=firestore.client()

	start_date = dt.datetime(2018, 10,1)
	end_date = dt.datetime(2018, 10,31)

	total_days = (end_date - start_date).days + 1 #inclusive 5 days

	for day_number in range(total_days):
		
		current_date = (start_date + dt.timedelta(days = day_number)).date()
		x=str((current_date))

		anio=x.split('-')[0]
		mes=x.split('-')[1]
		dia=x.split('-')[2]
		day=dia+'-'+mes+'-'+anio

		print(day)

		productos_local = db.collection(u'modelos_historico').document(day).collection('modelos').get()

		for lo in productos_local:

			
			movimiento=lo.to_dict()['movimiento']

			_color=movimiento['color']
			origen=movimiento['origen']
			destino=movimiento['destino']
			talla=movimiento['talla']
			modelo=movimiento['modelo']
			cantidad=movimiento['cantidad']

			print(_color,origen,destino,talla,modelo,cantidad)

			_color=Color.objects.get(nombre__iexact=_color).id

		
			origen=Local.objects.get(nombre__iexact=origen).id
			destino=Local.objects.get(nombre__iexact=destino).id
			talla=Talla.objects.get(nombre__iexact=talla).id
			modelo=Modelo.objects.get(nombre__iexact=modelo).id


			Movimiento(color_id=_color,origen_id=origen,destino_id=destino,talla_id=talla,modelo_id=modelo,cantidad=cantidad).save()

			print(_color,origen,destino,talla,modelo,cantidad)





	_usuarios = Usuarios.objects.all()
	serializer =  UsuariosSerializer(_usuarios,many=True)
	return JsonResponse(serializer.data, safe=False)



def listaglobo(request):


	_data = HistorialGlobo.objects.all()
	serializer =  HistorialGloboSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



