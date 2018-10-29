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
from django.db.models import Max,Count,Sum
import simplejson
# Create your views here.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    
	print('ksksk')


def guarda(request):

	cred = credentials.Certificate("clave.json")

	firebase_admin.initialize_app(cred, {
	    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
	})

	db=firestore.client()

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

	productos_local = db.collection(u'modelos_historico').document('20-10-2018').collection('modelos').get()

	for lo in productos_local:
	
		colore=lo.to_dict()['movimiento']['color']



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

	return JsonResponse('ok')

def agregatotalesfirebase(request):

	fecha=str(datetime.date.today())

	cred = credentials.Certificate("clave.json")

	firebase_admin.initialize_app(cred, {
	    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
	})

	db=firestore.client()


	mo = Modelo.objects.filter().values('id','nombre')

	for m in range(len(mo)):

		x= Movimiento.objects.filter(modelo_id=mo[m]['id']).values('destino__nombre','modelo__nombre','color__nombre','talla__nombre').annotate(total=Sum('cantidad')).order_by('destino__nombre')

		for y in range(len(x)):

			_id=id_generator()+str(fecha)

			data={
				u'cantidad':x[y]['total'],
				u'color':x[y]['color__nombre'],
				u'modelo':x[y]['modelo__nombre'],
				u'destino':x[y]['destino__nombre'],
				u'talla':x[y]['talla__nombre']
			}

			doca= db.collection(u'totales').document(_id+fecha)

			doca.set(data)


	return JsonResponse('ok', safe=False)


def listaglobo(request):


	_data = HistorialGlobo.objects.all()
	serializer =  HistorialGloboSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



def locales(request):

    serializer = LocalSerializer(Local.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def movimientos(request,local,modelo):

	# cred = credentials.Certificate("clave.json")

	# firebase_admin.initialize_app(cred, {
	#     'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
	# })

	# db=firestore.client()

	fecha=str(datetime.date.today())

	x= Movimiento.objects.filter(modelo__nombre__iexact=modelo,destino__nombre__iexact=local).values('color__nombre').annotate(total=Sum('cantidad')).order_by('destino__nombre',)


	for t in range(len(x)):

		x[t]['S']= Movimiento.objects.filter(modelo__nombre__iexact=modelo,destino__nombre__iexact=local,color__nombre=x[t]['color__nombre'],talla__nombre='S').count()
		x[t]['M']=Movimiento.objects.filter(modelo__nombre__iexact=modelo,destino__nombre__iexact=local,color__nombre=x[t]['color__nombre'],talla__nombre='M').count()
		x[t]['L']=Movimiento.objects.filter(modelo__nombre__iexact=modelo,destino__nombre__iexact=local,color__nombre=x[t]['color__nombre'],talla__nombre='L').count()
		
		print x[t]['S'],x[t]['M'],x[t]['L']

		x[t]['total']=x[t]['S']+x[t]['M']+x[t]['L']

	a= simplejson.dumps(ValuesQuerySetToDict(x))

	return HttpResponse(a, content_type="application/json")

			# for _co in range(len(x)):

			# 	data={
			# 		u'total':x[_co]['total'],
			# 		u'talla':x[_co]['talla__nombre'],
			# 	}

			# 	_id=id_generator()+str(fecha)

			# 	doca= db.collection(u'totales').document(mo[m]['nombre'])

			# 	doca.set({u'nombre':mo[m]['nombre']})

			# 	doca= db.collection(u'totales').document(mo[m]['nombre'])

			# 	doca.set({u'nombre':mo[m]['nombre']})
				
			# 	#.collection(co[c]['nombre']).document()

			# 	doca.set(data)

				

				#collection(co[c]['nombre']).document()

				#doca.set(data)



		

		


	
	a= simplejson.dumps(ValuesQuerySetToDict(mo))

	return HttpResponse(a, content_type="application/json")
