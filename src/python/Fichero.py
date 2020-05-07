#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:36:49 2020

@author: victor
"""
import sys
import numpy as np

def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 3:
        print("Uso: {} fichname number".format(sys.argv[0]))
        sys.exit(0)
    nombre = sys.argv[1]
    numeros= int(sys.argv[2])
    fichero = open(nombre,'w')
    for i in range(0,numeros):
        num = np.random.randint(99999)
        fichero.write(str(num) + '\n')
    fichero.close()
if __name__ == '__main__':
    main()
