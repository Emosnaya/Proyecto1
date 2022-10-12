from random import randint
import time
import numpy as np

def bubbleSort(A):
    tamanio = len(A)
    i = tamanio-1
    j = 0
    for i in range (tamanio-1, i<0,-1):
        for j in range (0,tamanio-1):
            if(A[j] > A[j + 1]):
                aux = A[j]
                A[j] = A[j + 1]
                A[j + 1] = aux
        
A = []
for i in range(500):
    A.append(randint(-1000,1001))

start = time.time()
print("ARREGLO DESORNDENADO")
print(A)
bubbleSort(A)
end = time.time()
print("ARREGLO ORDENADO")
print(A)
print()
print(f'El tiempo de ejecucio es {end-start}')