# Ejercicio 1: Suma de elementos
    # Escribe un programa que tome un arreglo de números y calcule la suma de todos los elementos.

import random

Array = []

for i in range(10):
    num = random.randint(0,10)
    Array.append(num)

suma = 0 

for i in Array:
    suma += i
    
print(" El arreglo inicial es:", Array)
print("La suma de los elementos del arreglo es:", suma)


    
