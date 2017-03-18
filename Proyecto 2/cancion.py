"""PROYECTO 2
# DESCRIPCIÓN: Creación de la clase canción, la cuál permitirá instanciar canciones para luego
ser almacenadas.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from pathlib import Path
from PyQt5.QtCore import QFile

class Cancion(object):
	def __init__(self,title,artist,file):
		self.titulo = title
		self.artista = artist
		self.archivo = file

	def es_igual(self,cancion):
		#  COMPARA SI UNA CANCION(self) ES IGUAL A OTRA POR TITULO
		# Y ARTISTA.
		if self.titulo == cancion.titulo and self.artista == cancion.artista:
			return True
		else:
			return False

	def es_menor_titulo(self,cancion):
		#  COMPARA SI UNA CANCION(self) ES MENOR A OTRA POR TITULO,
		# SI SON IGUALES, LOS COMPARA POR ARTISTA.
		if self.titulo == None and self.artista == None and self.archivo == None:
			# Si el self es el centinela, pues este será mayor que la canción.
			return False
		elif cancion.titulo == None and cancion.artista == None and cancion.archivo == None:
			# Si la cancion es el centinela, pues será mayor que el self.
			return True
		elif self.titulo < cancion.titulo:
			return True
		elif self.titulo == cancion.titulo:
			if self.artista < cancion.artista:
				return True
			else:
				return False
		else:
			return False

	def es_menor_artista(self,cancion):
		#  COMPARA SI LA CANCION(self) ES MENOR A OTRA POR ARTISTA,
		# SI SON IGUALES, LOS COMPARA POR TITULO.
		if self.titulo == None and self.artista == None and self.archivo == None:
			return False
		elif cancion.titulo == None and cancion.artista == None and cancion.archivo == None:
			return True
		elif self.artista < cancion.artista:
			return True
		elif self.artista == cancion.artista:
			if self.titulo < cancion.titulo:
				return True
			else:
				return False
		else:
			return False