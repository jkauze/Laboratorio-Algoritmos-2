"""PROYECTO 2
# DESCRIPCIÓN: Creación de la clase lista y nodo, la cual consiste en
crear las listas de reproducción.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from cancion import Cancion

class NodoLista(object):
	def __init__(self,anterior,cancion,nex):
		self.siguiente = nex
		self.elemento = cancion
		self.anterior = previous

class ListaReproduccion(object):
	def __init__(self):
		self.count = 0
		self.nill = NodoLista(None, Cancion(None,None,None), None)
		self.nill.siguiente = self.nill
		self.nill.anterior = self.nill
		self.proxima = self.nill

	def agregar(self,cancion):
		# AGREGA CANCIONES A LA LISTA DE REPRODUCCIÓN, SI LA
		# CANCIÓN ESTÁ REPETIDA NO LA AGREGA.
		if cancion.es_igual(self.proxima.elemento) == False:
			self.proxima = self.nill
			self.proxima = NodoLista(self.proxima.anterior, cancion, self.proxima)
			self.proxima.anterior.siguiente = self.proxima
			self.proxima.siguiente.anterior =self.proxima 
			self.count += 1
		else:
			print("La canción está repetida")
		return self.proxima

	def agregar_final(self,cancion):
		# AGREGA CANCIONES JUSTO ANTES DEL ELEMENTO h DE LA LISTA PARA QUE SEA LA ULTIMA
        	self.proxima.anterior = NodoLista(self.proxima.anterior, cancion)
            	self.proxima.anterior.anterior.siguiente = self.proxima.anterior #Porque el proxima.anterior.anterior, es el anterior original,
		return self.proxima.anterior

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
			x = x.siguiente
		for i in range(m):
		# Añade las canciones a R desde el último apuntado, hasta la mitad
			R.agregar(x)
			x = x.anterior
		for i in range(n): 
		# Añade a L desde el anterior a la última canción añadida a R hasta el
		# la primera canción de la lista
			L.agregar(x)
			x = x.anterior
		a = self.nill.siguiente
		x1 = L.nill.siguiente
		x2 = R.nill.siguiente
		if comparacion == "es_menor_titulo":
			for i in range(p,r+1):
				if x1.elemento.es_menor_titulo(x2.elemento) == True:
					a.elemento = x1.elemento
					x1 = x1.siguiente
					a = a.siguiente
				else:
					a.elemento = x2.elemento
					x2 = x2.siguiente
					a = a.siguiente
		else:
			for i in range(p,r+1):
				if x1.elemento.es_menor_artista(x2.elemento) == True:
					a.elemento = x1.elemento
					x1 = x1.siguiente
					a = a.siguiente
				else:
					a.elemento = x2.elemento
					x2 = x2.siguiente
					a = a.siguiente

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

	def eleminar(self,tituloCancion):
		# Elimina una canción buscandola por el titulo
		x = self.nill
		eliminar = False
		for i in range(self.count):
			# Recorre la lista para ver si encuentra la cancion
			if x.elemento.titulo == tituloCancion:
				x.anterior.siguiente = x.siguiente
				x.siguiente.anterior = x.anterior
				self.count -= 1
				eliminar = True
			else:
				x = x.siguiente
		if eliminar == False:
			print("No se ha encontrado la canción")
		else:
			print("La canción "+tituloCancion+" fue eliminada")
