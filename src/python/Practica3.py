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
# Código main:
def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 2:
        print("Uso: {} in out1 out".format(sys.argv[0]))
        sys.exit(0)
ficheroEntrada = sys.argv[1]
with open(ficheroEntrada,'r') as reader:
    for line in reader:
        numeros.append(int(line))
t0 = time.time_ns()
sinRepeticiones1=list(set(numeros))
t1 = time.time_ns()
t2 = time.time_ns()
sinRepeticiones2=dict.fromkeys(numeros).keys()
t3 = time.time_ns()

 
if __name__ == '__main__':
    main()
