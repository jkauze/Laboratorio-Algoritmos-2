"""PROYECTO 2
# DESCRIPCIÓN: Creación de la clase lista y nodo, la cual consiste en
crear las listas de reproducción.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from cancion import Cancion

class NodoLista(object):
	def __init__(self,anterior,cancion,siguiente):
		self.next = siguiente
		self.song = cancion
		self.previous = anterior

class ListaReproduccion(object):
	def __init__(self):
		self.count = 0
		self.nill = NodoLista(None, Cancion(None,None,None), None)
		self.nill.next = self.nill
		self.nill.previous = self.nill
		self.proximo = self.nill

	def agregar(self,cancion):
		# AGREGA CANCIONES A LA LISTA DE REPRODUCCIÓN, SI LA
		# CANCIÓN ESTÁ REPETIDA NO LA AGREGA.
		if cancion.es_igual(self.proximo.song) == False:
			self.proximo = self.nill
			self.proximo = NodoLista(self.proximo.previous, cancion, self.proximo)
			self.proximo.previous.next = self.proximo
			self.proximo.next.previous =self.proximo 
			self.count += 1
		else:
			print("La canción está repetida")
		return self.proximo

	def agregar_final(self,cancion):
		# AGREGA CANCIONES JUSTO ANTES DEL ELEMENTO PROXIMO DE LA LISTA PARA QUE SEA LA ULTIMA
		self.proximo.previous = NodoLista(self.proximo.previous, cancion, self.proximo)
		self.proximo.previous.previous.next = self.proximo.previous #Porque el proximo.previous.previous, es el previous original,
		return self.proximo.previous

	def merge(self,p,q,r,comparacion):
		# Funcion merge del mergesort, que particiona y ordena
		# los elementos de la lista.
		n = q - p + 1
		m = r - q
		L = ListaReproduccion()
		R = ListaReproduccion()
		x = self.nill
		for i in range(r):
		# Apunta al ultimo elemento, para añadirlo a R
			x = x.next
		for i in range(m):
		# Añade las canciones a R desde el último apuntado, hasta la mitad
			R.agregar(x)
			x = x.previous
		for i in range(n): 
		# Añade a L desde el anterior a la última canción añadida a R hasta el
		# la primera canción de la lista
			L.agregar(x)
			x = x.previous
		a = self.nill.next
		x1 = L.nill.next
		x2 = R.nill.next
		if comparacion == "es_menor_titulo":
			for i in range(p,r+1):
				if x1.cancion.es_menor_titulo(x2.cancion) == True:
					a.cancion = x1.cancion
					x1 = x1.next
					a = a.next
				else:
					a.cancion = x2.cancion
					x2 = x2.next
					a = a.next
		else:
			for i in range(p,r+1):
				if x1.cancion.es_menor_artista(x2.cancion) == True:
					a.cancion = x1.cancion
					x1 = x1.next
					a = a.next
				else:
					a.cancion = x2.cancion
					x2 = x2.next
					a = a.next

	def mergesort(self,p,r,comparacion):
		# Funcion que se utilizara para realizar las respectivas
		# ordenaciones.
		if p < r:
			q = (p+r)//2
			self.mergesort(p,q,comparacion)
			self.mergesort(q+1,r,comparacion)
			self.merge(p,q,r,comparacion)

	def ordenar_artista(self):
		# Metodo que ordena por artista las canciones de la lista
		# circular.
		self.mergesort(1,self.count,"es_menor_artista")

	def ordenar_titulo(self):
		# Metodo que ordena por titulo las canciones de la lista
		# circular.
		self.mergesort(1,self.count,"es_menor_titulo")

	def eliminar(self,tituloCancion):
		# Elimina una canción buscandola por el titulo
		x = self.nill
		eliminar = False
		for i in range(self.count):
			# Recorre la lista para ver si encuentra la cancion
			if x.cancion.title == tituloCancion:
				x.previous.next = x.next
				x.next.previous = x.previous
				self.count -= 1
				eliminar = True
			else:
				x = x.next
		if eliminar == False:
			print("No se ha encontrado la canción")
		else:
			print("La canción "+tituloCancion+" fue eliminada")
