#   Ejercicio 20: Implementar un Arbol Binario
    #   Crea una clase NodoArbol y una clase ArbolBinario. Implementa métodos para insertar elementos, recorrer el árbol en orden (inorder) y buscar un elemento.

class NodoArbol():
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario():
    def __init__(self, dato):
        self.raiz = NodoArbol(dato)

    def __agregar_nodo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(dato)
            else:
                self.__agregar_nodo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(dato)
            else:
                self.__agregar_nodo(nodo.derecha, dato)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo 
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        
    def __recorrer_inorder(self, nodo):
        if nodo is not None:
            self.__recorrer_inorder(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__recorrer_inorder(nodo.derecha)


    def agregar(self, dato):
        self.__agregar_nodo(self.raiz, dato)

    def inorder(self):
        print("Imprimiendo arbol inorden: ")
        self.__recorrer_inorder(self.raiz)
        print("")
        
    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


arbol = ArbolBinario(5)
arbol.agregar(2)
arbol.agregar(3)
arbol.agregar(4)
dato = int(input("Agrega algo al arbol: "))
valor = arbol.agregar(dato)
arbol.inorder()
arbol.agregar(5)
arbol.agregar(6)
arbol.agregar(7) 
arbol.inorder()

busqueda = int(input("Busca algo en el arbol: ")) 
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(busqueda, "no existe")
else:
    print(busqueda, "si existe")



        

            


            





            