def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

print(f'Resultado de la multiplicacion: {multiplicar(3, 5)}')
print(f'Resultado de la multiplicacion: {multiplicar(3, 5, 7)}')