class ColaEspecial(object):
    def __init__(self, tamañoInicial):
        self.cola =  []
        self.nItems = 0
    
    def mostrar_elementos(self):
        return print(len(self.cola))
        
    def agregar(self, dato):
        if len(self.cola) <= 10:
            self.cola.append(dato)
        elif len(self.cola) == 10:
            for i in range(10 - 1, 0, -1):
                self.cola.pop(self.cola[i])  
                self.cola.append(dato)

                        
        print(self.cola) 
            
    def __str__(self):
        return f"Arreglo({self.cola})"
            
    def eliminar(self, dato):
        self.cola.pop(dato)
        
