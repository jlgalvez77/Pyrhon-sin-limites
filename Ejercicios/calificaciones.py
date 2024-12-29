calificacion = int(input('Introduce la calificación'))

if calificacion >= 9 and calificacion <= 10:
    print(f'La calificación es A')
elif calificacion >= 8 and calificacion < 9:
    print('La calificación es B')
elif calificacion >= 7 and calificacion < 8:
    print('La calificación es C')
elif calificacion >= 6 and calificacion < 7:
    print('La calificación es D')
elif calificacion >= 0 and calificacion < 6:
    print('La calificación es F')
else:
    print('Valor Incorrecto')