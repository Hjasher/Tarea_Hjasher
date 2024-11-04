import math

class Rectangulo():
    def __init__(self, largo, altura, ancho):
        self._largo = largo
        self._altura = altura
        self._ancho = ancho
    def area(self):
        return self._largo * self._altura
    
    def perimetro(self):
        return (self._largo + self._ancho) * 2
    
    def diagonales(self):
        diagonal = math.sqrt(self._largo ** 2 + self._ancho ** 2)
        return round(diagonal, 4) 

rectangulo = Rectangulo(4,8,3)
rectangulo2 = Rectangulo(5,2,1)

print("El area del rectangulo 1 es:", rectangulo.area(), ", el perimetro es:", rectangulo.perimetro(),", las diagonales del rectangulo 1 miden:", rectangulo.diagonales())
print("El area del rectangulo 2 es:", rectangulo2.area(), ", el perimetro es:", rectangulo2.perimetro(), ", las diagonales del rectangulo 2 miden:", rectangulo2.diagonales())