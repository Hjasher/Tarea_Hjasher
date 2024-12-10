# Ejercicio 10: Historial de Navegador
    #   Implementa una pila para simular el historial de navegación en un navegador. Agrega una operación para “ir hacia atrás”.

class HistorialNavegacion():
    def __init__(self):
        self.historial = []

    def visitar(self, url):
        self.historial.append(url)
        print("Visitando:",url)

    def ir_atras(self):
        if len(self.historial) > 1:
             self.historial.pop()
             print("Regresando a la pagina:", self.historial[-1]) 
        else: 
             print("El historial está vacío, no hay mas paginas por mostrar")

navegador = HistorialNavegacion()
navegador.visitar("https://github.com/")
navegador.visitar("https://github.com/Hjasher")
navegador.visitar("https://github.com/Hjasher/Tarea_Hjasher")
navegador.ir_atras()
navegador.ir_atras()
navegador.ir_atras()


