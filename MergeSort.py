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

        
A =[-342,432,123,-3,-23,43,32,-50]
MergeSort(A,0,3)
print(A)