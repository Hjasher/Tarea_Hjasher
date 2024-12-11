#   Ejercicio 14: Reorganizar una cola
    #   Dada una cola de números, escribe un programa que reorganice los elementos para que los números pares queden al principio y los impares al final.

import random

cola = []
pares = []
impares = []

for i in range(10):
    num = random.randint(0,10)
    cola.append(num)

def organizar_pares_impares(cola):
    for i in cola:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    cola_organizada = pares + impares 

    return cola_organizada 


Organizar = organizar_pares_impares(cola)
print("La cola original es:",cola)
print("La cola organizada con los numeros pares a un lado y los impares al otro, sería:",Organizar)







