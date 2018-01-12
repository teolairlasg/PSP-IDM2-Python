#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#Librería para el volcado de datos en binario
import pickle 

filename = "/tmp/prueba-binario.txt"
fichero = open(filename, 'wb')
variable = ["Melchor","Gaspar","Baltasar"]
pickle.dump(variable,fichero)
fichero.close()

fichero = open(filename, 'rb')
leido = pickle.load(fichero)

print(leido[1])
