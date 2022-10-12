#busqueda Binaria iterativa
#Para redondear un número al entero anterior o posterior, 
#se pueden utilizar las funciones floor() y ceil(), 
#que están incluidas en la biblioteca math. 
#Estas funciones sólo admiten un argumento 
#(el número o el cálculo a redondear) y devuelven valores enteros.
import math
from random import randint
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

    
A = []
for i in range(500):
    A.append(randint(-1000,1001))

x=20
izquierda=0
derecha=499
print(BusquedaBinIter(A,x,izquierda,derecha))