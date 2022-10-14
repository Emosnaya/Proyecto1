
import math
from random import randint
import time
from unittest import result


def busquedaLineal(A,n,x):
	encontrado=-1
	for k in range(n+1):
		if A[k] == x:
			encontrado=k
	return encontrado


A = []
for i in range(250000):
    A.append(randint(-1000,1000))
	
x=-20
start = time.time()
resultado = busquedaLineal(A,len(A)-1,x)
end = time.time()
if(resultado == -1):
	print(f'No se encontro el valor {x} en el arreglo')
else:
	print(f'Se encontro el valor {x} en la posicion {resultado}')
	print(f'el tamanio del arreglo es de {len(A)} y el tiempo de ejecucion fue {end-start}')
