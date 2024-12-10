#   Ejercicio 12: Simular una fila de banco
    #   Usa una cola para simular la atención al cliente en un banco. Cada cliente tiene un número asignado y se atiende en orden.

class Banco():
    def __init__(self):
        self.cola = []
        self.indice = [] 
        self.codigo = 0
    def cola_vacia(self):
        return len(self.cola) == 0 
    
    def ingreso_cliente(self, nombre_cliente):
        self.codigo += 1
        self.cola.append(nombre_cliente)
        self.indice.append(self.codigo)

        if len(self.cola) >= 2:
            print("Cabina ocupada, tome asiento y espere su turno")
        else:    
            self.atendiendo_cliente(nombre_cliente)
        
    
    def atendiendo_cliente(self,cliente):
        print("Atendiendo al cliente:",cliente,"con el numero de turno:",self.indice[0])


    def siguiente_cliente(self):
        self.cola.pop(0)
        self.indice.pop(0)
        print("Siguiente en la cola porfavor")
        if not self.cola_vacia():
            self.atendiendo_cliente(self.cola[0])
        else:
            print("No hay mas clientes esperando")

banco = Banco()
banco.ingreso_cliente("Hjasher Medina")
banco.ingreso_cliente("Carlos Medina")
banco.siguiente_cliente()
banco.ingreso_cliente("Maria Carranza")
banco.ingreso_cliente("Moises Carranza")
banco.ingreso_cliente("Irma Valladares")
banco.ingreso_cliente("luis Turcios")
banco.ingreso_cliente("Javier Muñoz")
banco.siguiente_cliente()
banco.siguiente_cliente()
banco.siguiente_cliente()
banco.siguiente_cliente()
banco.siguiente_cliente()
banco.siguiente_cliente()




        
        



