#busqueda Binaria iterativa
#Para redondear un número al entero anterior o posterior, 
#se pueden utilizar las funciones floor() y ceil(), 
#que están incluidas en la biblioteca math. 
#Estas funciones sólo admiten un argumento 
#(el número o el cálculo a redondear) y devuelven valores enteros.
import math
from random import randint


def busquedaLineal(A,n,x):
	encontrado=-1
	for k in range(n+1):
		if A[k] == x:
			encontrado=k
	return encontrado


A = []
for i in range(500):
    A.append(randint(-1000,1001))

print(busquedaLineal(A,499,20))