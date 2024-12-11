#   Ejercicio 15: Ordenar Cola
    #   Escribe un programa que use solo operaciones de cola (enqueue y dequeue) para ordenar los elementos de una cola.

from collections import deque  

def ordenar_cola(cola):  
    cola_ordenada = deque()  

    while cola:  
        elemento = cola.popleft()      

        while cola_ordenada and cola_ordenada[-1] > elemento:  
            cola.append(cola_ordenada.pop())  
        
        cola_ordenada.append(elemento)  

    return cola_ordenada  

cola_original = deque([3, 1, 4, 2])  
print("Cola original:", list(cola_original))  

cola_ordenada = ordenar_cola(cola_original)  
print("Cola ordenada:", list(cola_ordenada)) 