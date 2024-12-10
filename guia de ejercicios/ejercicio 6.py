# Ejercicio 6: Implementacion Basica de una Pila
    #   Crea una clase Pila que implemente las operaciones básicas: push, pop y peek. Prueba la clase añadiendo y quitando elementos.

class Pila():
    def __init__(self):
        self.items = []

    def lista_vacia(self):
        return len(self.items) == 0
    
    def push(self,elemento):
        self.items.append(elemento)
    
    def pop(self):
        if not self.lista_vacia():
            self.items.pop()
        else:
            print("La pila está vacía")

    def peek(self):
        if not self.lista_vacia():
            print("El elemento de la cima es:",self.items[-1])
        else: 
            return "La pila está vacia"
        
# Esta funcion solo la hice para probar 
    def tamano_pila(self):
        return len(self.items)

pila = Pila()
print("Tamaño inicial de la pila:",pila.tamano_pila())
pila.push(1)
pila.push(2)
pila.push(3)
print("Tamaño de la pila despues de ingresar elementos:",pila.tamano_pila())
pila.pop()
pila.pop()
pila.pop()
pila.pop()
print(pila.peek())
print("Tamaño final de la pila:",pila.tamano_pila())

        
    





    

    