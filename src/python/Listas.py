#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Wrapper python para llamar a la función implementada en C.
'''
# Wrapper python para llamar a la función implementada en C.
import ctypes, os
def Listas(lista):
    # Objeto correspondiente a la función dentro de la biblioteca.
    funcLista = LIBList.Listas
    
    # Prototipo de la función: De la lista sin elementos duplicados, 
    #le pasamos un puntero a int. Observa que ctypes no define punteros a datos que
    # no sean c_char, c_wchar y c_void, por lo que hay que crearlos con POINTER. 
    funcLista.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int,
                          ctypes.POINTER(ctypes.c_int)]
    
    # Valor devuelto por la función (se puede eliminar, pues es el
    # comportamiento por defecto).
    funcLista.restype = ctypes.POINTER(ctypes.c_int)
    
    # Puesto que ctypes espera que el primer parámetro sea instancia
    # de punteros a c_int (es decir, instancias LP_c_int), según el
    # prototipo de la función, no podemos usar directamente lista 
    # ya que es de tipo list y no instancias de
    # LP_c_int. Lo que hacemos es definir salida como un array de valores
    # c_int, con tantos elementos como tiene lista.
    longitud=(ctypes.c_int*1)()
     # Llamada a la función de la biblioteca compartida.
    salida1=funcLista((ctypes.c_int * len(lista))(*lista), len(lista),longitud)
    
    
    
    # Vamos a devolver una lista. Para eso, hacemos una copia de la lista de
    # entrada. Podríamos devolver directamente «salida», pero sería un objeto de
    # ctypes tal y como lo hemos definido, con lo que una simple orden
    # «print(salida)» no nos mostraría su contenido sino su tipo. Queda más
    # "elegante" devolver algo como la entrada.
    listaout=[]
    aux = longitud[0]
    # Copiamos a dicho vector de salida el resultado de la función.
    for i in range(aux):
      listaout.append(salida1[i])
      
    # Devolvemos el vector de salida.
    return listaout
    
    
    
if __name__ == "Listas":
    # Cargamos la biblioteca compartida en ctypes.
    LIBList = ctypes.CDLL (os.path.abspath(os.path.join(os.path.dirname(__file__),  "../C/libListas.so.1")))



