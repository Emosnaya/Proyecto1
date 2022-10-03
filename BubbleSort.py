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
        
A = np.random.randint(-1000,1000, size=(20)) 
print(A)
bubbleSort(A)
print(A)
