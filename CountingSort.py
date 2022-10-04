from random import randint

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
    
#A=[9,-1,21,4,0,-3,-2,40,10,35] #lista propuesta por la práctica
A = []
for i in range(200):
    A.append(randint(-1000,1001))
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
    
print("Lista Ordenada", LO) #Se Imprime la lista original
print("Lista Original", A) #Se Imprime la lista original
