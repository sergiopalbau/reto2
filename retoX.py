import requests
import time
# ------------------------------------------------
def peticion (url, datos):
    '''
    hacemos una peticion POST al servidor con las coordenadas

    '''
    respuesta = requests.post(url,json=datos)
    como_json = respuesta.json()
    #print (datos)
    salida = como_json["status"]
    fallo = "Intenténtalo de nuevo, malandriner nunca se rinde"
    print (datos, salida)
    

    #time.sleep(3)

url='https://donde-esta-supercoco-delineas.vercel.app/api/reto/2'
datos= {"solution":"{2.0,3.5}"}
peticion (url, datos) 
