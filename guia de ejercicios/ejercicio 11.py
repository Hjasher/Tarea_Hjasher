#   Ejercicio 11: Implementacion Basica de una Cola
    #     Crea una clase Cola que implemente las operaciones básicas: enqueue, dequeue y peek.

class Cola():
    def __init__(self):
        self.cola = []

    def cola_vacia(self):
        return len(self.cola) == 0

    def enqueue(self, elemento):
        return self.cola.append(elemento)
    
    def dequeue(self):
        if not self.cola_vacia():
            print("Sacando al elemento:",self.cola.pop(0))
        else:
            print("La cola está vacía")

    def peek(self):
        if not self.cola_vacia():
            print("El primer elemento en la lista es:", self.cola[0])
        else:
            print("La cola está vacía")

cola = Cola()
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.peek()
cola.dequeue()
cola.peek()
cola.dequeue()
cola.dequeue()
cola.peek()