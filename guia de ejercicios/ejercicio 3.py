# Ejercicio 3: Invertir un Arreglo
    # Crea una función que reciba un arreglo y devuelva un nuevo arreglo con los elementos en orden inverso.

import random
Array = []

for i in range(10):
    num = random.randint(0,10)
    Array.append(num)

def inverso(Arreglo):
    nuevo_array = []
    for i in range(len(Arreglo) - 1, -1, -1 ):
        num = Arreglo[i]
        nuevo_array.append(num)
    return nuevo_array

Arreglo_invertido = inverso(Array) 
print("El arreglo original es:",Array)
print("El arreglo invertido es:",Arreglo_invertido)


