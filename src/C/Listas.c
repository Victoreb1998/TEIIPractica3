#include <stdio.h>
#include <stdlib.h>
#include "Listas.h"

int compare_ints(const void* a, const void* b)
{
	
	return (*(int *)a - *(int *)b);

}

int* Listas(int * lista, const int size,int * longitudFinal)
{
	
	int temp[size];
	int j=0;
	qsort(lista,size,sizeof(int),compare_ints);
	for(int i=0; i<size-1;i++)
		if(lista[i] != lista[i+1])
			temp[j++]=lista[i];
	temp[j++] = lista[size-1];
	int * salida = (int*)malloc(j*sizeof(int));
	for(int i=0;i<j;i++) {
        salida[i] = temp[i];
    }
    longitudFinal[0] = j;
    return salida;
}
