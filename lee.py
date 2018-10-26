import firebase_admin
from firebase_admin import credentials,firestore
import string
import random


cred = credentials.Certificate("clave.json")

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
})

db=firestore.client()

locales = db.collection(u'locales').get()

productos_local = db.collection(u'modelos_historico').document(u'20-10-2018').collection('modelos')

for l in locales:

	local = l.to_dict()['nombre']

	print(local)

	productos = productos_local.where(u'movimiento.destino', u'==', local).get()

	for p in productos:
	
		print(p.to_dict()['movimiento'])







# for l in locales:

#     print(l.id)

# 	for p in productos:

# 	    print( doc.to_dict()['movimiento'])


# 	    destino = doc.to_dict()['movimiento']['destino']

