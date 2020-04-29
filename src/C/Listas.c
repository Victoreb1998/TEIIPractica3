#include <stdio.h>
#include <stdlib.h>
#include "mult.h"

// Función que multiplica todos los elementos de un vector «vin» de tamaño
// «size» por un factor de escala «scale», dejando el resultado en el vector
// «vout».
int* Listas(int * lista, const int size)
{
    int i;
	int aux = size;
    for(i=0;i<aux;i++) {
        for(j=i+1; j < aux; j++){
			if(lista[i] == lista[j]){
				for(k=j; k<aux; k++){
					lista[k]=lista[k+1];
				}
				aux--;
				j--;
			}
		}
    }
    
    return lista;
}
