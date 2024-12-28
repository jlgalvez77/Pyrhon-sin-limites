# Calcular el area y el perimetro de un rectangulo pidiendo el alto y el ancho
# por consola

alto = int(input('Introduce el alto del rectangulo: '))
ancho = int(input('Introduce el ancho del rectagulo: '))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area: {area}')
print(f'Perimetro: {perimetro}')