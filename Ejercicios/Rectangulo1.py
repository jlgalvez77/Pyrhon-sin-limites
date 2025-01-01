class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    

base = float(input('Introduce la base del rectangulo: '))
altura = float(input('Introduce la altura del triangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.area()}')