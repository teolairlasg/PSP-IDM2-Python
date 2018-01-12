#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#Crear un programa de sincronización
#con ficheros usando fork y exclusión mútua

import fcntl
import time
import os

fichero = open("/tmp/pruebasEj1.txt","w+")
pid = os.fork()

if (pid == 0): #Código proceso hijo
	print("Proceso",os.getpid(),"solicitando acceso...")
	fcntl.flock(fichero,fcntl.LOCK_EX)
	mensaje = "Hijo:"+str(os.getpid())+" Mi padre es: "+str(os.getppid())+"\n"
	fichero.seek(0,2)
	fichero.write(mensaje)
	time.sleep(5)
	print("Proceso hijo liberando recurso...")
	fcntl.flock(fichero,fcntl.LOCK_UN)
	os._exit(0)
else:
	time.sleep(3)
	print("Proceso",os.getpid(),"solicitando acceso...")
	fcntl.flock(fichero,fcntl.LOCK_EX)
	mensaje = "Soy el padre "+str(os.getpid())+"\nMi hijo es: "+str(pid)+"\n"
	fichero.seek(0,2)
	fichero.write(mensaje)
	time.sleep(1)
	print("Proceso padre liberando recurso...")
	fcntl.flock(fichero,fcntl.LOCK_UN)
	os.wait()

fichero.seek(0)	
print(fichero.read())
fichero.close()







