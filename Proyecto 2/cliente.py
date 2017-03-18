"""PROYECTO 2
# DESCRIPCIÓN: Creación del cliente.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor
from arrayT import ArrayT

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)

	canciones = open("entrada.txt","r")
	n = int(canciones.readline())
	lista = ArrayT(n)
	can = canciones.readlines()

	for x in range(n):
		t = can[x].strip("\n")
		p = t.split("\t")
		lista[x] = p

	for x in lista:
		c = Cancion(x[0],x[1],x[2])
		rep.__playlist.agregar(c)

	#############
	# Menu loop #
	#############

	while True:
		print("REPRODUCTOR DE KAUZE Y DAVID\
				1.Listar canciones\
				2.Agregar para sonar justo después de la canción actual\
				3.Agregar para sonar justo antes de la canción actual\
				4.Ordenar lista de reproducción por artista\
				5.Ordenar lista de reproducción por titulo\
				6.Eliminar canción por titulo\
				7.Mostrar opciones\
				8.Salir")
		opcion = input("-----> INTRODUCIR OPCIÓN: ")
		if opcion == 1:
			x = rep.__playlist #Lista de Reproducción
			y = x.proxima.siguiente #Nodo
			print("Titulo,Artista")
			for i in range(x.count):
				print(y.elemento.titulo+","+y.elemento.artista)
			continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
		elif opcion == 2:
			try:
				c = Cancion(input("Titulo de la Canción: "),input("Artista de la Cancion: "),input("Archivo: "))
				rep.sonarDespues(c)
				print("-----> Canción Agregada")
				continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
			except:
				print("-----> Canción Inválida")
				continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------") 
		elif opcion == 3:
			try:
				c = Cancion(input("Titulo de la Canción: "),input("Artista de la Cancion: "),input("Archivo: "))
				rep.sonarAntes(c)
				print("-----> Canción Agregada")
				continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
			except:
				print("-----> Canción Inválida")
				continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------") 
		elif opcion == 4:
			rep.__playlist.ordenar_artista()
			print("-----> Lista Ordenada por artista")
			continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
		elif opcion == 5:
			rep.__playlist.ordenar_titulo()
			print("-----> Lista Ordenada por titulo")
			continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
		elif opcion == 6:
			titulo = input("Titulo de la canción: ")
			rep.eliminar(titulo)
			continuar = input("--------PRESIONE CUALQUIER LETRA PARA CONTINUAR--------")
		elif opcion == 7:
			pass
		elif opcion == 8:
			break

	############
	# Fin menu #
	############

	sys.exit(app.exec_())