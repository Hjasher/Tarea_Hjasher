class Array():
    def __init__(self):
        self.Autos = ["Toyota", "Mazda", "Honda", "Nissan", "Ferrari", "Hyundai"]
    
    def  cantidad_vehiculos(self):
        print("La cantidad de vehiculos disponibles es: ",len(self.Autos))


    def agregar_auto(self,auto):
        self.Autos.append(auto)
        print("Se a agregado el vehiculo:", auto)
        print("La nueva lista de vehiculos es:", self.Autos)


    def eliminar_auto(self,auto):
        if auto in self.Autos: 
            indice = self.Autos.index(auto)
            self.Autos.remove(auto)
            print("Se a eliminado el vehiculo", auto, "de la posicion ", indice)
            print("La nueva lista es:", self.Autos)
        else:
            print("El vehiculo no se encuentra en la lista")


    def modificar_auto(self, indice, nuevo_auto):
        if 0 <= indice < len(self.Autos):
            auto_inicial = self.Autos[indice]
            self.Autos[indice] = nuevo_auto
            print("Se ha modificado el vehiculo",auto_inicial, "por el vehiculo",nuevo_auto)
            print(self.Autos)
        else:
            print("El indice esta fuera del rango 0 -", len(self.Autos))


  

    def cambiar_orden(self):
        self.Autos.reverse()
        print("Se ha cambiado el orden de la lista")
        print("El nuevo orden de la lista es:",self.Autos)


    def contar_autos(self,auto):
        posiciones = [i for i, f in enumerate(self.Autos) if f == auto]
        cantidad = len(posiciones)
        return cantidad, posiciones


    def filtrar_autos(self,letra):
        autos_filtrados = [f for f in self.Autos if f.startswith(letra)]
        posiciones = [i for i, f in enumerate(self.Autos) if f.startswith(letra)]
        return autos_filtrados, posiciones

   
    def buscar_vehiculo(self,auto):
        if auto in self.Autos:
            return self.Autos.index(auto)
        else:
            return -1
        
    def mostrar_autos(self):
        print("La lista de vehiculos es: ", self.Autos)
        




