""" Proyecto 1
DESCRIPCION: El objetivo del proyecto es el de hacer un estudio experimental de algoritmos
de ordenamientos sobre diferentes conjuntos de datos. Algunos de los algoritmos que debe
implementar son parte del estado del arte y son ampliamente usados. Una vez realizadas las
pruebas solicitadas se quiere que haga un análisis de los resultados.

Autores: David Segura y Jesus Kauze"""

import math
from heap_functions import heap_sort

#VALORES INICIALES:

size_threshold = 10

# MEDIAN-OF-3 QUICKSORT:

def Partition(A,p,r,x):
    i = p-1
    j = r
    while True:
        while A[j] >= x:
            j = j - 1
        while A[i] <= x:
            i = i + 1
        if i < j:
            A[i],A[j] = A[j],A[i]
        else:
            return j

def Insertion_Sort(A):
    j = 1
    for x in range(j,len(A)):
        i = x-1
        key = A[x]
        while 0 <= i and A[i]>key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

def Quicksort_Loop(A,f,b):
    y = b - f
    while y > size_threshold:
        p = Partition(A,f,b,Median_of_3(A[f],A[f+int(y/2)],A[b-1]))
        if p-f >= b-p:
            b = p
            Quicksort_Loop(A,p,b)
        else:
            f = p
            Quicksort_Loop(A,f,p)

def Median_of_3(a,b,c):
    if a>b and b>c:
        return b
    elif b>a and a>c:
        return a
    else:
        return c

def Quicksort(A,f,b):
    Quicksort_Loop(A,f,b)
    Insertion_Sort(A)

A = [86,24,6,2,1,4,45,2]

#Quicksort(A,0,len(A))

# INTROSORT:

def Introsort_Loop(A,f,b,depth_limit):
    y = b - f
    while y > size_threshold:
        if depth_limit == 0:
            heap_sort(A)
        depth_limit = depth_limit - 1
        p = Partition(A,f,b,Median_of_3(A[f],A[f + int(y/2)],A[b-1]))
        Introsort_Loop(A,p,b,depth_limit)
        b = p

def Introsort(A,f,b):
    z = int(math.log(b-f,2))
    Introsort_Loop(A,f,b,2*z)
    Insertion_Sort(A)

#Introsort(A,0,len(A))

# QUICKSORT WITH 3 WAY PARTITIONING:

def Quicksort_3_way(A,l,r):
    i = l-1
    j = r
    p = l-1
    q = r
    v = A[r]
    if r <= 10:
        Insertion_Sort(A)
    else:
        while True:
            while A[i] < v:
                i += 1
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

#Quicksort_3_way(A,0,len(A)-1)
print(A)

#QUICKSORT_YAROSLAVSKIY

def QuicksortYaroslavskiy(A,left,right):
    y = right - left
    if y < len(A):
        Insertion_Sort(A)
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
        QuicksortYaroslavskiy(A,lef,l-1)
        QuicksortYaroslavskiy(A,l+1,g-1)
        QuicksortYaroslavskiy(A,g+1,right)

#QuicksortYaroslavskiy(A,0,len(A)-1)
print(A)

