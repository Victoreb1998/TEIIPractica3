#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Práctica TEII - Bloque 4 - Código de la sesión 3 de prácticas
'''

import sys
import time as t
import numpy as np
import matplotlib.pyplot as plt
from Listas import Listas
numeros = []
numerosaux=[]
tiemposSet=[]
tiemposDic=[]
tiemposC=[]
numerosProcesar=2000

def plot_values(x, y,y2,y3,width=0.5):
    
    plt.plot(x,y,color = 'g', label="Tiempo set") 
    plt.plot(x,y2,color = 'r', label="Tiempo Dic")
    plt.plot(x,y3,color = 'b', label="Tiempo C")       
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
ficheroEntrada = None
ficheroSalida = None
ficheroPDF = None

try:
    ficheroPDF = sys.argv[3]
    comprobacion = ficheroPDF.split(".")
    if (len(comprobacion)!=2 or comprobacion[1] != "pdf"):
        raise ValueError()
except:
    print("Debe de introducir un fichero pdf")
    sys.exit(-1)
    
try:
    ficheroSalida = sys.argv[2]
    #comprobamos que el fichero no tenga ninguna extension, si la tiene
    #pedimos que el usuario meta un nombre simple
    comprobacion = ficheroSalida.split(".")
    if (len(comprobacion)!=1):
        raise ValueError()
except:
    print("Debe de introducir simplemente un nombre")
    sys.exit(-2)
try:
    ficheroEntrada = sys.argv[1]
    with open(ficheroEntrada,'r') as reader:
        for line in reader:
            numeros.append(int(line))
    if (len(numeros)!=200000):
        raise ValueError()
except:
    print("El fichero de entrada debe existir")
    sys.exit(-3)
        
sinRepeticiones1=[]


while(numerosProcesar <= 200000):
	#nos guardamos la cantidad de números con la que trabajamos
	#para luego mostrarla en la gráfica
    numerosaux.append(numerosProcesar)
    #cogemos los numerosProcesar elementos de la lista original
    #Para trabajar con ellos
    aux=numeros[0:numerosProcesar]
    
    t0 = t.time_ns()
    list(set(aux))
    t_exec1 = (t.time_ns()-t0)/1.0e9
    
    t2 = t.time_ns()
    dict.fromkeys(aux).keys()
    t_exec2 = (t.time_ns()-t2)/1.0e9
    
    t3 = t.time_ns()
    sinRepeticiones1=Listas(aux)
    t_exec3 = (t.time_ns()-t3)/1.0e9
    
    tiemposC.append(t_exec3)
    tiemposSet.append(t_exec1)
    tiemposDic.append(t_exec2)
    numerosProcesar+=2000
   
plot1 = plot_values(numerosaux, tiemposSet,tiemposDic,tiemposC,width=0.5)
plot1.savefig(ficheroPDF,bbox_inches='tight')

fichero = open(ficheroSalida,'w')
for numero in sinRepeticiones1:
        fichero.write(str(numero) + '\n')

 
if __name__ == '__main__':
    main()
