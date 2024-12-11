#   Ejercicio 13: Cola Circular
    #   Implementa una cola circular con una longitud fija. Incluye métodos para añadir y eliminar elementos.

class ColaCircular():
    def __init__(self,tamaño):
        self.tamaño = tamaño
        self.cola = [None] * tamaño
        self.frente = -1
        self.final = -1

    def encolar(self, elemento):
        if (self.final + 1) % self.tamaño == self.frente:
            self.frente = (self.frente + 1) % self.tamaño
        if self.frente == -1:
            self.frente = 0 
        self.final = (self.final + 1) % self.tamaño
        self.cola[self.final] = elemento
        print("Encolando el elemento:",elemento)

    def desencolar(self):
        if self.frente == -1:
            print("La cola está vacía")
        else:
            elemento = self.cola[self.frente]
            if self.frente == self.final:
                self.frente = -1
                self.final = -1
            else:
                self.frente = (self.frente + 1) % self.tamaño
            print("Desencolando el elemento:",elemento)
            return elemento


    def mostrar_cola(self):
        if self.frente == -1:
            print("La cola está vacia")
        else:
            print("La cola es:",self.cola)


cola = ColaCircular(5)
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.mostrar_cola()
cola.encolar(5)
cola.mostrar_cola()
cola.encolar(4)
cola.mostrar_cola()
cola.encolar(5)
cola.encolar(6)
cola.encolar(7)
cola.encolar(8)
cola.encolar(9)
cola.mostrar_cola()


            

        
        

    