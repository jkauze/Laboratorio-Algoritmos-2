"""PROYECTO 2
# DESCRIPCIÓN: Creación de la clase canción, la cuál permitirá instanciar canciones para luego
ser almacenadas.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from pathlib import Path
from PyQt5.QtCore import QFile

class Cancion(object):
	def __init__(self,titulo,artista,archivo):
		self.title = titulo
		self.artist = artista
		self.file = archivo

	def es_igual(self,cancion):
		#  COMPARA SI UNA CANCION(self) ES IGUAL A OTRA POR TITULO
		# Y ARTISTA.
		if self.title == cancion.titulo and self.artist == cancion.artista:
			return True
		else:
			return False

	def es_menor_titulo(self,cancion):
		#  COMPARA SI UNA CANCION(self) ES MENOR A OTRA POR TITULO,
		# SI SON IGUALES, LOS COMPARA POR ARTISTA.
		if self.title == None and self.artist == None and self.file == None:
			# Si el self es el centinela, pues este será mayor que la canción.
			return False
		elif cancion.title == None and cancion.artist == None and cancion.file == None:
			# Si la cancion es el centinela, pues será mayor que el self.
			return True
		elif self.title < cancion.titulo:
			return True
		elif self.title == cancion.titulo:
			if self.artist < cancion.artista:
				return True
			else:
				return False
		else:
			return False

	def es_menor_artista(self,cancion):
		#  COMPARA SI LA CANCION(self) ES MENOR A OTRA POR ARTISTA,
		# SI SON IGUALES, LOS COMPARA POR TITULO.
		if self.title == None and self.artist == None and self.file == None:
			return False
		elif cancion.title == None and cancion.artist == None and cancion.file == None:
			return True
		elif self.artist < cancion.artista:
			return True
		elif self.artist == cancion.artista:
			if self.title < cancion.titulo:
				return True
			else:
				return False
		else:
			return False