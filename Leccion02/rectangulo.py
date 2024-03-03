'''
Instrucciones de la tarea:
- En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectangulo
para ello deberemos crear las siguientes variables:

alto(int)
ancho(int)

- El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir
el resultado en el siguiente formato.

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perimetro : <perimetro>
'''

alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el alto: '))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area: {area}')
print(f'Perimetro: {perimetro}')