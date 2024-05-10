from math import *

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return sqrt(self.raio) * pi
    def calcular_perimetro(self):
        return 2 * pi * self.raio

r = float(input("Valor do raio: "))
circulo = Circulo(r)
print(f"Área do circulo: {circulo.calcular_area():.2f} cm².")
print(f"Perímetro do circulo: {circulo.calcular_perimetro():.2f} cm.")