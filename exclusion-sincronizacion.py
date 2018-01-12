#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import fcntl
import os
import time

filename = "/tmp/prueba.txt"

#Solicitar acceso a recurso. Bloquearlo.
print("Solicitando acceso a",filename)
fichero = open(filename, 'w')
fcntl.flock(fichero,fcntl.LOCK_EX)
fichero.seek(0,2) ##posicionarme al final del fichero
mensaje = "\nSoy el proceso"+str(os.getpid())
fichero.write(mensaje)
time.sleep(2)
#Desbloquear recurso, en este caso fichero.
print("Liberando recurso",filename)
fcntl.flock(fichero,fcntl.LOCK_UN)
fichero.close()