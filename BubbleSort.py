from random import randint
import time

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
for i in range(250000):
    A.append(randint(-1000,1000))

start = time.time()
bubbleSort(A)
end = time.time()
print(len(A))
print(f'El tiempo de ejecucion es {end-start}')
