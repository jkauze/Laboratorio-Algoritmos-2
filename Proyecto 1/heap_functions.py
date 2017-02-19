"""
# Descripcion: Implementacion de las funciones necesarias para
				El ordenamiento Heapsort.
# Autor: Jesus Kauze y David Segura
# email: 12-10273@usb.ve y 13-11341@usb.ve
"""
from arrayT import ArrayT

def heapify(array, i, lenght):
	hijo_izquierdo = left(i)
	hijo_derecho = right(i)
	el_mayor = i
	if hijo_izquierdo < lenght and array[hijo_izquierdo]> array[i]:
		el_mayor = hijo_izquierdo
	if hijo_derecho < lenght and array[hijo_derecho] > array[el_mayor]:
		el_mayor = hijo_derecho
	if el_mayor != i:
		swap(array, el_mayor, i)
		heapify(array, el_mayor, lenght)
	return array

def build_max_heap(array):
	i = (len(array)// 2)
	while i >= 0:
		heapify(array, i, len(array))
		i = i-1
	return array

def heap_sort(array):
	build_max_heap(array)
	i = len(array) -1 
	while i >= 1:
		swap(array, 0, i)
		heapify(array, 0 ,i)
		i=i-1

def swap(array, i, j):
	array[i],array[j] = array[j],array[i]
	return array

def dequeue(array):
    if len(array)<1:
    	print("El arreglo debe tener más de un elemento")
    aux_array=ArrayT(len(array)-1)
    for x in range(0,len(array)-1):
    	aux_array[x] = array[x+1]
    heapify(aux_array,0,len(aux_array))
    return(array[0],aux_array)


def parent(i):
    return ((i + 1) // 2) -1

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))