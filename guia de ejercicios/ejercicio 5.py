# Ejercicio 5: Eliminar Duplicados
    # Crea una función que elimine los valores duplicados de un arreglo y devuelva un nuevo arreglo con valores únicos.

import random

Array = []

for i in range(10):
    num = random.randint(0,10)
    Array.append(num)

def eliminar_duplicados(Arreglo):

    elementos_vistos = set()
    elementos_duplicados = set()

    for i in Arreglo:
        if i in elementos_vistos:
            elementos_duplicados.add(i)
        else:
            elementos_vistos.add(i)

    return list(elementos_vistos)

Eliminar_duplicados = eliminar_duplicados(Array)
print("El arreglo original es:",Array)
print("El arreglo eliminando los datos duplicados es:",Eliminar_duplicados)


    



