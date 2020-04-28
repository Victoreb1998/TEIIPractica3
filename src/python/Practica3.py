#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Práctica TEII - Bloque 4 - Código de la sesión 3 de prácticas
'''

import sys
import time as t
import numpy as np
import matplotlib.pyplot as plt
numeros = []
numerosaux=[]
tiemposSet=[]
tiemposDic=[]
numerosProcesar=2000

def plot_values(x, y,y2, width=0.5):
    
    plt.plot(x,y,color = 'g', label="Tiempo set") 
    plt.plot(x,y2,color = 'r', label="Tiempo Dic")     
    plt.title('Tiempos de uso')
    plt.legend()
    plt.xlabel('Numero de Valores')
    plt.ylabel('Tiempos')
    return plt
    
    
# Código main:
def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 4:
        print("Uso: {} in out1 out".format(sys.argv[0]))
        sys.exit(0)
ficheroEntrada = sys.argv[1]
ficheroSalida = sys.argv[2]
ficheroPDF = sys.argv[3]
with open(ficheroEntrada,'r') as reader:
    for line in reader:
        numeros.append(int(line))
sinRepeticiones1=[]
sinRepeticiones2=[]
while(numerosProcesar <= 200000):
    numerosaux.append(numerosProcesar)
    aux=numeros[0:numerosProcesar]
    t0 = t.time_ns()
    sinRepeticiones1=list(set(aux))
    t_exec1 = (t.time_ns()-t0)/1.0e9
    t2 = t.time_ns()
    sinRepeticiones2=dict.fromkeys(aux).keys()
    t_exec2 = (t.time_ns()-t2)/1.0e9
    tiemposSet.append(t_exec1)
    tiemposDic.append(t_exec2)
    numerosProcesar+=2000
    
t = np.linspace(0,200000,2000) 
   
plot1 = plot_values(numerosaux, tiemposSet,tiemposDic, width=0.5)
plot1.savefig(str(ficheroPDF)+'.pdf',bbox_inches='tight')

fichero = open(ficheroSalida,'w')
for numero in sinRepeticiones1:
        fichero.write(str(numero) + '\n')

 
if __name__ == '__main__':
    main()
