#busqueda Binaria iterativa
#Para redondear un número al entero anterior o posterior, 
#se pueden utilizar las funciones floor() y ceil(), 
#que están incluidas en la biblioteca math. 
#Estas funciones sólo admiten un argumento 
#(el número o el cálculo a redondear) y devuelven valores enteros.
import math
from random import randint
import time
def BusquedaBinIter(A,x,izquierda,derecha):
    while izquierda <= derecha:
        medio=math.floor((izquierda+derecha)/2)
        if (A[medio] == x):
            return medio
        elif (A[medio] < x):
            izquierda = medio+1

        else:
                derecha=medio-1
    return -1

# Counting sort (Código Original) 
def CreaLista(k): #Esta función crea una lista de apoyo
    L=[]
    for i in range(k+1):
        L.append(0)
    return L

#Algoritmo de ordenamiento

def CountingSort(A,k): # A es la lista y k es el valor máximo de la lista
    C=CreaLista(k)
    B=CreaLista(len(A)-1)
    for j in range(0,len(A)):
        C[A[j]]=C[A[j]]+1
    for i in range (1,k+1):
        C[i]=C[i]+C[i-1]
    for j in range (len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
    return B #Retorna el la lista de apoyo B la cual es la que está ordenada
    

A = []
for i in range(500):
    A.append(randint(-1000,1000))
N=[]
P=[]
LO=[]
for i in range (0,len(A)):
    if(A[i]<0):
        N.append(A[i]*-1)
    else:
        P.append(A[i])

if (len(N)!=0):
    aux=[]
    aux= CountingSort(N,max(N)) #Se manda a llamar la función de ordenamiento
    for i in range (len(aux)-1,-1,-1):
        LO.append(aux[i]*-1)
    
if (len(P)!=0):
    aux=[]
    aux= CountingSort(P,max(P)) #Se manda a llamar la función de ordenamiento
    for i in range (0,len(aux)):
        LO.append(aux[i])
    


x=20
izquierda=0
derecha=len(LO)-1
start = time.time()
resultado = BusquedaBinIter(LO,x, izquierda,derecha)
end = time.time()
if(resultado == -1):
    print(f'No se encontro el valor {x} en el arreglo')
else:
    print(f'Se encontro el valor {x} en la posicion {resultado}')
    print(f'El tamanio del arreglo es de {len(A)} y el tiempo de ejecucion fue de {end-start}')