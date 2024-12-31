# Definir una tupla
frutas = ('Naranja', 'Manzana', 'Pera')
print(frutas)
# Saber la longitud de la tupla
print(len(frutas))
# Acceder a un elemento de la tupla
print(frutas[0])
# Acceder a un rango de elementos
print(frutas[0:2]) # No incluye el último elemento
# Recorrer una tupla
for fruta in frutas:
    print(fruta, end=' ')
# No se puede modificar una tupla
# frutas[0] = 'Plátano' # Error
frutaLista = list(frutas)
frutaLista[0] = 'Plátano'
frutas = tuple(frutaLista)
print('\n', frutas)
# Eliminar la tupla
del frutas