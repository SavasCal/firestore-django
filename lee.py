import firebase_admin
from firebase_admin import credentials,firestore
import string
import random
import datetime as dt

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

	productos_local = db.collection(u'modelos_historico').document(day).collection('modelos')

	modelos = db.collection(u'modelos').get()

	loc = db.collection(u'locales').get()

	for lo in loc:

		loca = lo.to_dict()['nombre']

		for m in modelos:

			# modelo = m.to_dict()['nombre']

			# print(modelo)

			productos = productos_local.where(u'movimiento.local', u'==', loca).get()

			for p in productos:
			
				print(p.to_dict()['movimiento'])







# for l in locales:

#     print(l.id)

# 	for p in productos:

# 	    print( doc.to_dict()['movimiento'])


# 	    destino = doc.to_dict()['movimiento']['destino']

