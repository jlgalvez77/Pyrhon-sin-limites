def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
print(f'Factorial de 5: {factorial(5)}')