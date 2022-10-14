from random import randint
import time

def intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp
def particionar(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if (A[j]<=x):
            i=i+1
            intercambia(A,i,j)
    intercambia(A,i+1,r)
    return i+1
def Quicksort(A,p,r):
    if(p<r):
        q=particionar(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)


A = []
for i in range(250000):
    A.append(randint(-1000,1000))


start = time.time()
Quicksort(A,0,len(A)-1)
end = time.time()
print("Arreglo ordenado")
print(f'El tiempo de ejecucion es {end-start} {len(A)}')