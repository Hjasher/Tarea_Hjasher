# Ejercicio 9: Pila de Numeros 
    #   Simula una calculadora que use una pila para realizar operaciones básicas (+, -, *, /). Los números y operaciones se ingresan como una lista.

def calculadora(lista):
    pila = []

    for elemento in lista:
        if isinstance(elemento, (int, float)):
            pila.append(elemento)
        elif elemento in "+-*/":
            b = pila.pop()
            a = pila.pop()
            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            elif elemento == "/":
                resultado = a / b
            pila.append(resultado)
    return pila.pop()

lista = [2, 3, "-", 2, "*"] # aqui tenemos esto: (2-3) * 2
lista2 = [3, 1, '+', 2, '*', 7, '-', 3, "/"] # aqui tenemos esto otro: (((3+1) * 2) - 7) / 3 
resultado = calculadora(lista)
resultado2 = calculadora(lista2)
print("El resultado de la operacion (2-3) * 2 es:",resultado)
print("El resultado de la operacion (((3+1) * 2) - 7) / 3 es:",resultado2)
        
