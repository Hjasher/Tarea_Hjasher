#   Ejercicio 16: Implementar una Lista Enlazada Simple 
    #   Crea una clase Nodo y una clase ListaEnlazada. Implementa métodos para agregar elementos al final, eliminar un elemento, y buscar un elemento.
class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None 

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None 

    def agregar(self,valor):
        nuevo_nodo = nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        previo = None
        while actual and actual.valor != valor:
            previo = actual 
            actual = actual.siguiente
        if actual == None:
            return 
        if previo == None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente  

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end= " -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.mostrar()
lista.eliminar(3)
lista.mostrar()
lista.eliminar(1)
lista.mostrar()

        
        

 