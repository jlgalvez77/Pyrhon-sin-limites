# set
planetas = {'Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno'}
print(planetas)
# Saber la longitud del set
print(len(planetas))
# Revisar si un elemento está presente
print('Tierra' in planetas)
# No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# Eliminar elementos
planetas.remove('Tierra')
print(planetas)
# Eliminar elementos con discard
planetas.discard('Jupiter')
print(planetas)
# Limpiar el set
planetas.clear()
print(planetas)
# Eliminar el set
del planetas
