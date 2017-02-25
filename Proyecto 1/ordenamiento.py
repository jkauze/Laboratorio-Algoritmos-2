""" Proyecto 1
DESCRIPCION: El objetivo del proyecto es el de hacer un estudio experimental de algoritmos
de ordenamientos sobre diferentes conjuntos de datos. Algunos de los algoritmos que debe
implementar son parte del estado del arte y son ampliamente usados. Una vez realizadas las
pruebas solicitadas se quiere que haga un análisis de los resultados.

Autores: David Segura y Jesus Kauze"""

import math 
from random import *
from arrayT import ArrayT

#VALORES INICIALES:

size_threshold = 10

# MEDIAN-OF-3 QUICKSORT:
def Partition(A,p,r,x):
    i = p
    j = r
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
            	break
        while True:
            i = i + 1
            if A[i] >= x:
            	break
        if i < j:
            A[i],A[j] = A[j],A[i]
        else:
            return j

def Insertion_Sort(A, b, c):
    for x in range(b,c):
        i = x-1
        key = A[x]
        while 0 <= i and A[i]>key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

def Insertion_Sort2(A,left,right):
    for x in range(left,right+1):
        i = x-1
        key = A[x]
        while 0 <= i and A[i]>key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

def Quicksort_Loop(A,f,b):
    while (b-f) > size_threshold: #arreglos mayores a 10 elementos
        p = Partition(A,f,b,Median_of_3(A[f],A[f+int((b-f)/2)],A[b-1]))
        if (p-f >= b-p):
            Quicksort_Loop(A,p,b)
            b = p
        else:
            Quicksort_Loop(A,f,p)
            f = p

def Median_of_3(a,d,c):
    b = []
    b.append(a)
    b.append(d)
    b.append(c)
    Insertion_Sort(b,0,len(b))
    return b[1]

def Quicksort_Median_of_3(A):
    b=len(A)
    f=0
    Quicksort_arreglo(A,f,b)

def Quicksort_arreglo(A,f,b):
    Quicksort_Loop(A,f,b)
    Insertion_Sort(A,f,b)

# INTROSORT: ##############################################33

def Introsort_Loop(A,f,b,depth_limit):
    while (b-f) > size_threshold:
        if depth_limit == 0:
            Heap_sort(A,f,b)
        depth_limit = depth_limit - 1
        p = Partition(A,f,b,Median_of_3(A[f],A[f + int((b-f)/2)],A[b-1]))
        Introsort_Loop(A,p,b,depth_limit)
        b = p

def Introsort(A):
    b=len(A)
    f=0
    Introsort_arreglo(A,f,b)

def Introsort_arreglo(A,f,b):
    z = int(math.log(b-f,2))
    Introsort_Loop(A,f,b,2*z)
    Insertion_Sort(A,f,b)

# QUICKSORT WITH 3 WAY PARTITIONING: ##############################

def Quicksort_3_Way_Partitioning(A):
    r = len(A)-1
    l = 0
    Quicksort_3_way(A,l,r)

def Quicksort_3_way(A,l,r):
    i = l-1
    j = r
    p = l-1
    q = r
    if r-l <= 10 and r-l > 0:
        Insertion_Sort2 (A,l,r)
    elif r <= l:
    	return
    else:
        v = A[r]
        while True:
            i += 1
            while A[i] < v:
                i += 1
            j -= 1
            while A[j] > v:
                j -= 1
                if j == l:
                    break
            if i >= j:
                break
            A[i],A[j] = A[j],A[i]
            if A[i] == v:
                p += 1
                A[p],A[i] = A[i],A[p]
            if A[j] == v:
                q -= 1
                A[j],A[q] = A[q],A[j]
        A[i],A[r] = A[r],A[i]
        j = i - 1
        i = i + 1
        k = l
        while k < p:
            A[k],A[j] = A[j],A[k]
            k += 1
            j -= 1
        k = r - 1
        while k > q:
            A[i],A[k] = A[k], A[i]
            k -= 1
            i += 1
        Quicksort_3_way(A,l,j)
        Quicksort_3_way(A,i,r)

#QUICKSORT_YAROSLAVSKIY #################################################

def QuicksortYaroslavskiy(A):
    right=len(A)-1
    left = 0 
    QuicksortYaroslavskiy_arreglo(A,left,right)

def QuicksortYaroslavskiy_arreglo(A,left,right):
    if right - left < 10:
        Insertion_Sort2(A,left,right)
    else:
        if A[left]>A[right]:
            p,q = A[right], A[left]
        else:
            p,q = A[left], A[right]
        l = left+1
        g = right-1
        k=l
        while k<=g:
            if A[k] < p:
                A[k],A[l] = A[l],A[k]  #Swap
                l = l+1
            else:
                if A[k] >= q:
                    while A[g] > q and k < g:
                        g = g-1
                    if A[g] >= p:
                        A[k],A[g] = A[g],A[k] #Swap
                    else:
                        A[k],A[g] = A[g],A[k]
                        A[k],A[l] = A[l],A[k]
                        l=l+1
                    g=g-1
            k = k + 1
        l = l-1
        g = g+1
        A[left],A[l] = A[l],p
        A[right],A[g] = A[g],q
        QuicksortYaroslavskiy_arreglo(A,left,l-1)
        QuicksortYaroslavskiy_arreglo(A,l+1,g-1)
        QuicksortYaroslavskiy_arreglo(A,g+1,right)

#MERGESORT #######################################################

def Mergesort(arreglo):
	k = 1
	N= len(arreglo)
	NuevoArreglo=ArrayT(N)
	while k<N:
		a,b,c = 0, k, min(2*k,N)
		while b<N:
			p,q,r = a,b,a
			while p!=b and q !=c:
				if arreglo[p] <= arreglo[q]:
					NuevoArreglo[r] = arreglo[p]
					r,p = r+1, p+1
				elif arreglo[q] <= arreglo[p]:
					NuevoArreglo[r]=arreglo[q]
					r,q = r+1, q+1
			while p != b:
				NuevoArreglo[r] = arreglo[p]
				r,p = r+1, p+1
			while q != c:
				NuevoArreglo[r] = arreglo[q]
				r,q = r+1, q+1
			r = a
			while r!=c:
				arreglo[r]=NuevoArreglo[r]
				r = r+1
			a,b,c = a + 2*k, b + 2*k, min(c + 2*k,N)
		k = k*2
	return NuevoArreglo

#HEAP_SORT #####################################################3

def heapify(array, i, lenght):
	hijo_izquierdo = left(i)
	hijo_derecho = right(i)
	el_mayor = i
	if hijo_izquierdo < lenght and array[hijo_izquierdo]>= array[i]:
		el_mayor = hijo_izquierdo
	if hijo_derecho < lenght and array[hijo_derecho] >= array[el_mayor]:
		el_mayor = hijo_derecho
	if el_mayor != i:
		swap(array, el_mayor, i)
		heapify(array, el_mayor, lenght)
	return array

def build_max_heap(array,f,b):
    n = len(array)
    for i in range(n//2,f-1,-1):
	    heapify(array, i, n)
    return array

def Heap_sort(array,f,b):
    build_max_heap(array,f,b)
    i = b-f
    while i >= f+1:
        swap(array, 0, i)
        heapify(array, 0 ,i)
        i=i-1


def Heapsort(A):
    Heap_sort(A,0,len(A)-1)

def swap(array, i, j):
	array[i],array[j] = array[j],array[i]
	return array

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))

# QUICKSORT RANDOMIZADO ######################################################

def Partition2(A,p,r):
    x = A[r]
    i = p -1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1 
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r]= A[r], A[i+1]
    return i+1 

def Randomized_Partition(A,p,r):
	i = randint(p,r)
	A[r],A[i]=A[i],A[r]
	return Partition2(A,p,r)

def quicksort_aleatorio(A,p,r):
	if p<r:
		q= Randomized_Partition(A,p,r)
		quicksort_aleatorio(A,p,q-1)
		quicksort_aleatorio(A,q+1,r)

def Randomized_Quicksort(A):
	p=0
	r=len(A)-1
	quicksort_aleatorio(A,p,r)
	return A