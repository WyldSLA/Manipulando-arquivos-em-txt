class Retangulo:
    def __init__(self, l=0, c=0):
        self.l = l
        self.c = c
    
    def area(self):
        area = self.l * self.c
        return area
    
    def perimetro(self):
        per = 2 * (self.l) + 2 *(self.c)
        return per


rt1 = Retangulo(20)

area = rt1.area()
per = rt1.perimetro()

print(f"Área: {area}cm² \nPerímetro: {per}cm")