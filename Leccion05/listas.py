# Crear una lista
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Imprimir la lista
print(nombres)
# Acceder a un elemento de la lista
print(nombres[0])
print(nombres[-1])

# Acceder a un rango
print(nombres[0:2]) # Sin incluir el indice 2
# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
# Desde el indice indicado hasta el final
print(nombres[1:])
# Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)
# Iterar la lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))
# Agregar un elemento a la lista
nombres.append('Lorenzo')
print(nombres)
# Insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)
# Eliminar un elemento
nombres.remove('Octavio')
print(nombres)
# Eliminar el ultimo valor de la lista
nombres.pop()
print(nombres)
# Eliminar un indice en especifico
del nombres[0]
print(nombres)
# Limpiar la lista
nombres.clear()
print(nombres)
# Borrar la lista por completo
del nombres
print(nombres) # Error porque la lista ya no existe