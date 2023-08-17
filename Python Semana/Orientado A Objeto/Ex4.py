class triangulo():
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self,):
        print(f'A área é: {(self.base * self.altura) / 2}')
triangulo1 = triangulo(5,7)
triangulo1.calcular_area()