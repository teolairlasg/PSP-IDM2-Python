#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

filename = "/tmp/prueba.txt"
fichero = open(filename, 'w')
fichero.write("Hola\nMundo.\nFichero.")
fichero.close()
fichero = open(filename, 'r')

n = 1
for linea in fichero.readlines():

	print(n,":",linea)
	n+=1



