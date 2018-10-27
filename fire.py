from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import firebase_admin
from firebase_admin import credentials,firestore
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

cred = credentials.Certificate("clave.json")

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://gamarra-e89b4.firebaseio.com'
})

db=firestore.client()

def guardafirebase(fecha,color,s,modelo,origen,destino,talla):

    _id=id_generator()+str(fecha)

    doc= db.collection(u'modelos_historico').document(fecha).collection('modelos').document(_id)
    
    data={
        u'movimiento':{
            u'cantidad':s,
            u'color':color,
            u'modelo':modelo,
            u'origen':u'Inicio',
            u'destino':destino,
            u'talla':talla
        },
        u'fecha':fecha

    }

    guarda=0

    if (s=='0' or s=='-' or color=='TOTAL'):

        guarda=1

        print('Ingrese...',s,color)

    if guarda==0:
    
        doc.set(data)

    return 'oK'



def leesheet(SPREADSHEET_ID,RANGE_NAME,modelo):

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:

        for m in range(len(values)):

            print(values[m])

            guardafirebase(u'20-10-2018',values[m][0],values[m][1],modelo,'Inicial',u'ALMACEN',u'S')
            guardafirebase(u'20-10-2018',values[m][0],values[m][2],modelo,'Inicial',u'ALMACEN',u'M')
            guardafirebase(u'20-10-2018',values[m][0],values[m][3],modelo,'Inicial',u'ALMACEN',u'L')
            guardafirebase(u'20-10-2018',values[m][0],values[m][4],modelo,'Inicial',u'TORRE',u'S')
            guardafirebase(u'20-10-2018',values[m][0],values[m][5],modelo,'Inicial',u'TORRE',u'M')
            guardafirebase(u'20-10-2018',values[m][0],values[m][6],modelo,'Inicial',u'TORRE',u'L')
            guardafirebase(u'20-10-2018',values[m][0],values[m][7],modelo,'Inicial',u'CANEPA',u'S')
            guardafirebase(u'20-10-2018',values[m][0],values[m][8],modelo,'Inicial',u'CANEPA',u'M')
            guardafirebase(u'20-10-2018',values[m][0],values[m][9],modelo,'Inicial',u'CANEPA',u'L')


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1o5931JEbZ3Buq0smb-QJA11Fs--SySlLaaoTa9GP9a4'
    RANGE_NAME = 'IBHET!A3:J19'

    hojas=[u'LAZO',u'IBHET',u'Isabella gasa',u'ISABELA',u'THAYSA',u'LETICIA',u'IBhet corto',u'tabitah',u'TRAPECIO',u'ESTER V',u'Isabella corto',u'PAMELA',u'IRINA','angela',u'VERONICA']

    for h in hojas:

        print(h)

        leesheet(SPREADSHEET_ID,h+'!'+'A3:J19',h)

if __name__ == '__main__':
    main()



