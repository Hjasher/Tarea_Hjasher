#   Ejercicio 17: Invertir una lista enlazada
    #   Crea un método en la clase ListaEnlazada para invertir el orden de los nodos.

class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None 

    def agregar(self, valor):
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

    def invertir(self):
        actual = self.cabeza
        previo = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo 
            previo = actual
            actual = siguiente
        self.cabeza = previo 


    def mostrar(self):
        actual = self.cabeza 
        while actual:
            print(actual.valor, end= " -> ")
            actual = actual.siguiente 
        print("None")


lista = ListaEnlazada()
lista.mostrar()
lista.agregar(1)
lista.agregar(2)
lista.mostrar()
lista.invertir()
lista.mostrar()
            

            

