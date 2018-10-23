from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse,JsonResponse
from app.serializers import *
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("/Users/xiencias/code/ania/clave.json")

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
})



# Create your views here.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    
	print('ksksk')



def listausuarios(request):


	db=firestore.client()

	doc= db.collection(u'colores').document(u'2TH2M3qAoCcOE8KydSG6')
	doc.set({
		u'oi':'ELessss',
		u'aieie':'www'

		})



	_usuarios = Usuarios.objects.all()
	serializer =  UsuariosSerializer(_usuarios,many=True)
	return JsonResponse(serializer.data, safe=False)



def listaglobo(request):


	_data = HistorialGlobo.objects.all()
	serializer =  HistorialGloboSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def guarda(request):


	estado= request.GET['estado']
	usuario= request.GET['usuario']



	_user = Usuarios.objects.get(nombre=usuario).id
	_estado= Estado.objects.get(nombre=estado).id

	id_hg= HistorialGlobo.objects.filter(usuario_id=_user).values('id').order_by('-id')[0]['id']

	globo=HistorialGlobo.objects.get(id=id_hg)

	ultimo_estado=globo.estado.nombre



	if ultimo_estado==estado:



		globo.fecha_fin=datetime.datetime.today()
		globo.save()

	else:

		id_hg= HistorialGlobo.objects.filter(usuario_id=_user).values('id').order_by('-id')[0]['id']

		globo=HistorialGlobo.objects.get(id=id_hg)

		globo.fecha_fin=datetime.datetime.today()

		globo.save()

		HistorialGlobo(usuario_id=_user,estado_id=_estado,fecha_inicio=datetime.datetime.today(),fecha_fin=datetime.datetime.today()).save()


	c= simplejson.dumps('ok')

	return HttpResponse(c, content_type="application/json")
