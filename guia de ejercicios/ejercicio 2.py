# Ejercicio 2: Maximo y Minimo 
    # Dado un arreglo de números, encuentra el valor máximo y el mínimo sin usar funciones predefinidas como max o min.

import random

Array = []

for i in range(10):
    numero = random.randint(0,10)
    Array.append(numero)

valor_maximo = Array[0]
valor_minimo = Array[0]

for i in Array:
    if i > valor_maximo:
        valor_maximo = i 
    if i < valor_minimo:
        valor_minimo = i

# De esta linea hasta la 44 fue algo que quise probar...        
cantidad_valor_maximo = 0 
cantidad_valor_minimo = 0 
posiciones_valor_maximo = []
posiciones_valor_minimo = []
indice = 0 

for i in Array:
    if i == valor_maximo:
        cantidad_valor_maximo += 1
        posiciones_valor_maximo.append(indice)
    if i == valor_minimo:
        cantidad_valor_minimo += 1
        posiciones_valor_minimo.append(indice)
    indice += 1

if len(posiciones_valor_maximo) > 1:
    palabra = "veces en el arreglo, en las posiciones"
else:
    palabra = "vez en el arreglo, en la posicion"
if len(posiciones_valor_minimo) > 1:
    palabra2 = "veces en el arreglo, en las posiciones"
else:
    palabra2 = "vez en el arreglo, en la posicion"



print(Array)
print("El valor maximo del arreglo es:",valor_maximo,"y este aparece",cantidad_valor_maximo,palabra, posiciones_valor_maximo) 
print("El valor minimo del arreglo es:",valor_minimo,"y este aparece",cantidad_valor_minimo,palabra2, posiciones_valor_minimo)









