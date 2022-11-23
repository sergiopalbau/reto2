
import string

#creamos una lista con el abecedario
abc= list(string.ascii_uppercase)

#añadimos a la lista una ultima posicion que es el espacio
abc.append (" ")

#valor del desplazamiento usado en la codificacion
desplazamiento = 5

#mensaje secreto
msg = "NVI EPVI YZ BVUOZGPBVOSZ"


#se convierte a lista el mensaje secreto
list_msg = list(msg)


#lista resultante con el mensaje decodificado
list_salida = []

#recorrer el mensaje codificado buscando cada elemento en la referencia
for c in list_msg:
    #creamos una lista donde buscamos que posicion ocupa cada caracter del mensaje secreto en la lista de referencia
    #list_salida.append (abc.index(c))
    
    #salto en la ejcucion del for cuando encotramos un espacio
    if abc.index(c) >= 26:  
       list_salida.append(" ") 
       continue

    indice = abc.index(c)
    #si superamos el tamaño de nuestra lista, hay que reposicionar para encontrar el caracter adecuado
    if  (indice+desplazamiento >=26):
        indice = (indice-26)
#    print (c,indice, indice+desplazamiento,abc[indice+desplazamiento])
    list_salida.append(abc[indice+desplazamiento])

salida = ''.join(list_salida)
print (salida)
   




