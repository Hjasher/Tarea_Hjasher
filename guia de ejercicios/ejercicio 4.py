# Ejercicio 4: Buscar un elemento
    # Escribe un programa que tome un arreglo y un número, y determine si el número está presente en el arreglo.

import random

Array = []

for i in range(10):
    num = random.randint(0,10)
    Array.append(num)

def buscar_numero(Arreglo, numero):
    cantidad_de_veces = 0
    indice = 0
    posiciones = []  
    for i in Arreglo:
        if i == numero:
            cantidad_de_veces += 1
            posiciones.append(indice)
        indice += 1 
# De la linea 22 a la linea 25, reutilicé parte de la prueba que hice en el ejercicio 2
    if cantidad_de_veces > 1:
        palabra = "veces en el arreglo, en las posiciones"
    else:
        palabra = "vez en el arreglo, en la posicion"

    print("Buscando el numero:",numero,"...")
    print("El numero",numero,"si está en el arreglo, aparece",cantidad_de_veces,palabra,posiciones)

print("El arreglo es:",Array)
Buscar_numero = buscar_numero(Array, 3)

