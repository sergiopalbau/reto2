import requests
import time
# ------------------------------------------------
def peticion (url, datos):
    '''
    hacemos una peticion POST al servidor con las coordenadas

    '''
    respuesta = requests.post(url,data=datos)
    como_json = respuesta.json()
    #print (datos)
    salida = como_json["status"]
    fallo = "Intenténtalo de nuevo, malandriner nunca se rinde"
    print (datos, salida)
    

    #time.sleep(3)

url='https://donde-esta-supercoco-delineas.vercel.app/api/reto/2'
datos= {"solution":"{2.0,3.5}"}
peticion (url, datos) 



pista ="3311014444"

#lista =[3.3,3.31,3.311,3.3110,3.31101,3.311014,3.3110144]
#lista2 = [33.1, 33.11, 33.110, 33.1101,33]

'''#separar la pista
for dig_lat in range(1,8):
    print (pista[0:dig_lat], pista[dig_lat:8])
'''
latitud =[]
for i in range (0,2):
    for j in range (i,(10-(i+1))):
         #print ("i",i,"j",j, "- "+pista[0:i+1] + '.' + pista[i+1:j+2])
         latitud.append(pista[0:i+1] + '.' + pista[i+1:j+2])
        #latitud.append('-'+ pista[0:i+1] + '.' + pista[i+1:j+2])  

#latitudes posibles sin filtrar solo positivas
#print (latitud)


coordenada = []

for i in latitud:
    pista2= pista[len(i)-1:10]
    tamaño = len(pista2)
    #print ("el tamaño es", tamaño)
    #print (i , " ** ",pista2)
    for j in range(0, tamaño-1):
        #print (pista2[0:j+1]+'.'+pista2[j+1:tamaño])
        #coordenada positiva
        coordenada.append([i,pista2[0:j+1]+'.'+pista2[j+1:tamaño]])
        #coordenada latitud negativa longitud positiva
        coordenada.append(['-'+i,pista2[0:j+1]+'.'+pista2[j+1:tamaño]])
        #coordenada latitud negativa longitud negativa
        coordenada.append(['-'+i,'-'+pista2[0:j+1]+'.'+pista2[j+1:tamaño]])
        #coordenada latitud positiva longitud negativa
        coordenada.append([i,'-'+pista2[0:j+1]+'.'+pista2[j+1:tamaño]])
#print (coordenada)

print ("tenemos una lista sin filtrar con ", len(coordenada),"elementos" )
contador = 0
for c in coordenada:
    
    cadenaLat = str(c[0])
    cadenaLon = str(c[1])
    dato ="{\"solution\":" "\"{"+cadenaLat+","+cadenaLon+"}\"}"
    print (contador)
    contador+=1
    datos= {"solution":"{2.0,3.5}"}
   # print (type(datos))
    #print ( print (type(dato)))
    peticion (url,dato)

     

