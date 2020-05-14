import jsonpickle
import os
import sys
from dbx import TransferData

access_token = os.environ['dropbox_token']

def loadJSON():

    transferData = TransferData(access_token)

    try:
        data = transferData.download_file('/users.json')
        obj = jsonpickle.decode(data)
        
        return(obj)
    except Exception as e:
        print(f"{e}", file=sys.stdout)
        return({})

def writeJSON(obj):

    transferData = TransferData(access_token)

    with open('users.json', 'w') as file:
        objJSON = jsonpickle.encode(obj)
        file.write(objJSON)
        file.close()
    
    transferData.upload_file('users.json', '/users.json')