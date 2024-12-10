# Ejercicio 8: Revertir una Cadena con una Pila
    #    Escribe una función que use una pila para invertir una cadena de texto.

def invertir_cadena(cadena):
    pila = [] 

    for char in cadena:
        pila.append(char)

    cadena_invertida = ""
    while pila:
        cadena_invertida += pila.pop()

    return cadena_invertida

cadena = "Hola mundo"
cadena2 = "Que honda"
print("Las cadenas originales son:",cadena,",",cadena2)
print("Las cadenas invertidas son:",invertir_cadena(cadena),",",invertir_cadena(cadena2))


    
