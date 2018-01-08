#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import os
import time

def imprimir_pid():
	print("Mi pid es:",os.getpid())

def lanzar_hijo():
	pid = os.fork()
	if pid == 0:
		imprimir_pid()
		os._exit(0)

while True:
	print("h: crear hijo")
	print("q: salir")
	opcion = input()
	if opcion == "h":
		print("Creando hijo...")
		lanzar_hijo()
		time.sleep(1)
	elif opcion == "q":
		break
	else: 
		continue