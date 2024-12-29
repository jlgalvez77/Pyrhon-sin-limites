valor = int(input('Escribe un valor'))
valor_minimo = 0
valor_maximo = 25

en_rango = valor >= valor_minimo and valor <= valor_maximo

if(en_rango):
    print('El dato está dentro de rango')
else:
    print('El dato está fuera de rango')