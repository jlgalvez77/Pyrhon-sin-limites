edad = int(input('Introduce tú edad'))

veintes = edad >= 20 and edad <= 30
treintas = edad >= 30 and edad <=40

if veintes or treintas:
    print('Dentro de rango')
else:
    print('Fuera de rango')