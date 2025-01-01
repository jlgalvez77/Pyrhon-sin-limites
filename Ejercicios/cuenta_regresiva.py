def cuenta_recursiva(numero):
    if numero > 0:
        print(numero)
        cuenta_recursiva(numero - 1)

cuenta_recursiva(5)