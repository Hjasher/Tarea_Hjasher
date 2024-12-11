#   Ejercicio 23: Contar Hojas en un Arbol Binario 
    #   Escribe una función que cuente cuántos nodos hoja (nodos sin hijos) tiene un árbol binario.

from collections import deque


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
                print("Agregado",dato,"a la izquierda de",nodo.dato)
            else:
                self.__agregar_nodo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(dato)
                print("Agregado",dato,"a la derecha de",nodo.dato)
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

    def __altura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self.__altura(nodo.izquierda)
            altura_derecha = self.__altura(nodo.derecha)
            return max(altura_izquierda, altura_derecha) +1 
        
    def altura(self):
        return self.__altura(self.raiz)


    def agregar(self, dato):
        self.__agregar_nodo(self.raiz, dato)

    def inorder(self):
        print("Imprimiendo arbol inorden: ")
        self.__recorrer_inorder(self.raiz)
        print("")
        
    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    
    def recorrer_por_niveles(self):
        if self.raiz is None:
            return
        
        queue = deque([self.raiz])
        while queue:
            nodo = queue.popleft()
            print(nodo.dato, end=", ")
            if nodo.izquierda:
                queue.append(nodo.izquierda)
            if nodo.derecha:
                queue.append(nodo.derecha)
        print("")
        

    def contar_nodos_en_nivel(self, nivel):
        if self.raiz is None:
            return 0
        
        queue = deque([(self.raiz, 0)])
        contador = 0
        while queue:
            nodo, nivel_actual = queue.popleft()
            if nivel_actual == nivel:
                contador += 1
            if nivel_actual < nivel:
                if nodo.izquierda:
                    queue.append((nodo.izquierda, nivel_actual + 1))
                if nodo.derecha:
                    queue.append((nodo.derecha, nivel_actual + 1))
        return contador
    
    def contar_hojas(self):
        if self.raiz is None:
            return
        queue = deque([self.raiz])
        contador = 0
        while queue:
            nodo = queue.popleft()
            if nodo.izquierda is None and nodo.derecha is None:
                contador +=1
            if nodo.izquierda:
                queue.append(nodo.izquierda)
            if nodo.derecha:
                queue.append(nodo.derecha)
        return contador




arbol = ArbolBinario(3)
arbol.agregar(2)
arbol.agregar(3)
arbol.agregar(4)

arbol.inorder()
arbol.agregar(5)
arbol.agregar(6)
arbol.agregar(7)
arbol.agregar(20) 
arbol.inorder()


dato = int(input("Agrega algo al arbol: "))
valor = arbol.agregar(dato)

busqueda = int(input("Busca algo en el arbol: ")) 
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(busqueda, "no existe")
else:
    print(busqueda, "si existe")

print("Arbol recorrido por niveles: ") 
arbol.recorrer_por_niveles()

nivel = int(input("Introduce el nivel para contar los nodos: "))
print(f"Número de nodos en el nivel {nivel}: {arbol.contar_nodos_en_nivel(nivel)}")

print("La cantidad de hojas que existen en el arbol es: ", arbol.contar_hojas())

print("La altura del arbol es: ",arbol.altura())