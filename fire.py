import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("clave.json")

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
})

db=firestore.client()

doc= db.collection(u'colores').document(u'2TH2M3qAoCcOE8KydSG6')
doc.set({
	u'oi':'djjd',
	u'aieie':'skskk'

	})