#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Práctica TEII - Bloque 4 - Código de la sesión 3 de prácticas
'''

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
numeros = []
tiemposSet=[]
tiemposDic=[]
numerosProcesar=2000
# Código main:
def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 3:
        print("Uso: {} in out1 out".format(sys.argv[0]))
        sys.exit(0)
ficheroEntrada = sys.argv[1]
ficheroSalida = sys.argv[2]
with open(ficheroEntrada,'r') as reader:
    for line in reader:
        numeros.append(int(line))
sinRepeticiones1=[]
sinRepeticiones2=[]
while(numerosProcesar <= 200000):
    aux=numeros[0:numerosProcesar]
    t0 = time.time_ns()
    sinRepeticiones1=list(set(aux))
    t1 = time.time_ns()
    t2 = time.time_ns()
    sinRepeticiones2=dict.fromkeys(aux).keys()
    t3 = time.time_ns()
    tiemposSet.append(t1-t0)
    tiemposDic.append(t3-t2)
    numerosProcesar+=2000

fichero = open(ficheroSalida,'w')
for numero in sinRepeticiones1:
        fichero.write(str(numero) + '\n')

 
if __name__ == '__main__':
    main()
