import time
from random import randint
#Funcion CountingSort
def countingSort(arr, exp1):

    #Se obtiene el tamaño del arreglo
    n = len(arr)

    #Contador de los positivos
    n1 = 0
    #Contador de los negativos
    n2 = 0

    #Se cuenta cuantos valores negativos y positivos existen en el arreglo
    for j in range(0, len(arr)):
        if arr[j] >= 0:
            n1 = n1+1
        else:
            n2 = n2+1
    
    #Se crean los arreglos de salida
    #El de los positivos
    output = [0] * (n1)
    #El de los negativos
    output2 = [0] * (n2)

    #Se crean las matrices de conteo
    #La de los positivos
    count = [0] * (10)
    #La de los negativos
    count2 = [0] * (10)    

    #Se hace la cuenta en cada matriz de conteo con sus condicionales en caso de quel valor sea positvo o negativo
    for i in range(0, n):
        index = arr[i]

        #En caso de que sea positivo, se cuente en la de los positivos
        if index >= 0:
            index = arr[i] // exp1
            count[index % 10] += 1
        #En caso de que sea negativo, se cuente en la de los negativos
        else:
            index = index*(-1)
            index = index // exp1
            count2[index % 10] += 1

    #Se realiza la suma en las matrices de conteo
    for i in range(1, 10):
        count[i] += count[i - 1]
        count2[i] += count2[i - 1]
        
    #Se hace el ordenamiento con sus condicionales en cada arreglo de salida, tanto para el arreglo de salida de los positivos como la de los negativos y se hace la resta correspondiente en su matriz de conteo
    i = n - 1
    while i >= 0:
        index = arr[i]
        if index >= 0:
            index = index// exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
        else:
            index = index * (-1)
            index = index // exp1
            output2[count2[index % 10] - 1] = arr[i]
            count2[index % 10] -= 1
        i -= 1
    
    #Se procede a inscribir los datos de los arreglos de salida en el arreglo original
    i = 0
    #En caso de que no hayan existido valores negativos en el arreglo, se iscribira unicamente el arreglo de salida de los positivos en el arreglo original
    if n2 == 0:
        for i in range(0, len(arr)):
            arr[i] = output[i]
    #En caso de que hayan existido valores negativos, se utilizaran dos auxiliares
    else:
        aux1 = 0
        aux2 = 0
        #Se utilizaran dos ciclos para inscribir el arreglo de salida de los negativos en la parte inicial del arreglo original y posteriormente se inscribira el arreglo de salida de los positivos despues de los negativos en el arreglo original
        for z in range(0, n2, 1):
            arr[aux1] = output2[z]
            aux1 = aux1 + 1
        for m in range(n2, len(arr), 1):
            arr[m] = output[aux2]
            aux2 = aux2 + 1

#Funcion RadixSort
def radixSort(arr):
    #Se encuentra el valor maximo del arreglo
    max1 = max(arr)
    #Se inicializa exp para las unidades para posteriormente incrementar acorde a las necesidades del algoritmo a ordenar
    exp = 1
    #Se inicializa contador el cual servirá para saber cuantos valores negativos tiene el arreglo
    contador = 0

    #Se realiza la función de countingSort
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    
    #Se calcula cuantos valores negativos tiene el arreglo
    for p in range(0, len(arr)):
        if arr[p] < 0:
            contador = contador + 1
    
    #En caso de que exista al menos un valor negativo, se hara uso de la funcion negativos
    if contador > 0:
        negativos(contador)
    
    #En caso de que el valor maximo sea menor o igual a 0, significa que todos los valores del arreglo son menores o iguales a 0
    if max1 <= 0:
        #Se hara uso de un arreglo de apoyo
        apoyo = arr
        #Se procedera a multiplicar el arreglo de apoyo por -1
        for k in range (0,len(apoyo)):
            apoyo[k] = apoyo[k]*(-1)
        #Se vuelve a calcular el valor maximo del arreglo ya que ahora todos son positivos
        max1 = max(apoyo)
        #Se realiza el ordenamiento como si todo el arreglo hubiese sido positivo
        while max1 / exp >= 1:
            countingSort(apoyo, exp)
            exp *= 10
        #Se procedera a multiplicar el arreglo por -1 para regresar a los valores que habia en un inicio
        for k in range (0,len(apoyo)):
            apoyo[k] = apoyo[k]*(-1)
        #Una vez este el arreglo ordenado se invertira ya que esta ordenado de forma ascendente (como si fuesen positivos) por lo que esta ordenado de forma descendente
        arr = apoyo.reverse()

#Funcion negativos, se hara uso de ella en caso de que exista al menos 1
def negativos(contador):
    #Se crea un arreglo auxiliar con 0's del tamaño de los valores negativos en el arreglo original
    arr2 = [0] * (contador)
    #Se usa el ciclo para inscribir todos los valores negativos del arreglo original en el auxiliar
    for i in range(0, contador):
        arr2[i] = arr[i]
    #Se inicializa una variable auxiliar que nos permitirá con un ciclo invertir el arreglo auxiliar para que este ordenado de forma ascendente y se inscribira al inicio del arreglo original, asi estara ordenado de forma ascendente todo este arreglo 
    aux = contador-1
    for j in range(0, contador):
        arr[aux] = arr2[j]
        aux = aux -1

#Declaracion del arreglo propuesto por la practica
#arr = [170, 45, 75, 90, 802, 24, 2, 66]
#Arreglo propuesto para su verificacion con los negativos
#arr = [432, -543, 213, 0, -432, 423, 54, -324, 23, 54, -5, -65, 99, -130]
arr = []
for i in range(200):
    arr.append(randint(-1000,1001))
start = time.time()
#Se llama a la funcion RadixSort
radixSort(arr)
end = time.time()
#Se imprime el arreglo
print("El arreglo ordenado es: ")
for i in range(len(arr)):
    print(arr[i],end=" ")

print("El tiempo que ha tardado en ejecutarse con el algoritmo de RadixSort es: ", end-start)