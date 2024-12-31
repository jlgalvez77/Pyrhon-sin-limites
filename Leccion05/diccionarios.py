# Diccionarios (key:value)
diccionario = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 28
}
print(diccionario)
# Saber la longitud del diccionario
print(len(diccionario))
# Acceder a un elemento del diccionario
print(diccionario['nombre'])
# Acceder a un elemento del diccionario con get
print(diccionario.get('nombre'))
# Modificar un valor del diccionario
diccionario['nombre'] = 'Karla'
print(diccionario)
# Recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer solo las claves
for termino in diccionario.keys():
    print(termino)

# Recorrer solo los valores
for valor in diccionario.values():
    print(valor)

# Comprobar si existe un elemento
print('nombre' in diccionario)

# Agregar un elemento
diccionario['pais'] = 'Mexico'
print(diccionario)

# Remover un elemento
diccionario.pop('pais')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario) # Error