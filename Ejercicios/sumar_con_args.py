def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(f'Resultado de la suma: {suma(3, 5)}')
print(f'Resultado de la suma: {suma(3, 5, 7)}')