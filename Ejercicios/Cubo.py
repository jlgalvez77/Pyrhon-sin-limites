class Cubo:
    def __init__(self, ancho, largo, alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.largo * self.alto
    
ancho = float(input('Introduce el ancho: '))
largo = float(input('Introduce el largo: '))
alto = float(input('Introduce el alto: '))
cubo = Cubo(ancho, largo, alto)
print(f'El volumen del cubo es: {cubo.calcular_volumen()}')