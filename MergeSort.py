import random
from random import randint
import time

def crearSubArreglo(A, indIzq, indDer):
	return A[indIzq:indDer+1]

def Merge(A,p,q,r):
	Izq = crearSubArreglo(A,p,q)
	Der = crearSubArreglo(A,q+1,r)
	i=0
	j=0
	for k in range(p,r+1):
		if(j>=len(Der)) or (i < len (Izq)and Izq[i] and Izq[i] < Der[j]):
			A[k]=Izq[i]
			i=i+1
		else:
			A[k]=Der[j]
			j=j+1
def MergeSort(A,p,r):
	if r - p > 0:
		q = int((p+r)/2)
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)

A = []
for i in range(250000):
    A.append(randint(-1000,1000))

start = time.time()
MergeSort(A,0,len(A)-1)
end = time.time()
print("Arreglo Ordenado")
print(f'El tiempo de ejecucion es {end-start}')