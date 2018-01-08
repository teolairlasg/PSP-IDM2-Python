#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import os

def imprimir_pid():
	print("Mi pid es:",os.getpid())

pid = os.fork()

if pid == 0:
	print("Soy el hijo")
	imprimir_pid()
	os._exit(0)
else:
	print("Soy el Padre")
	imprimir_pid()
	print("Mi hijo tiene el pid:",pid)
print("Acabando...")