class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}')


persona1 = Persona('Jose', 'Galvez', 47)
# persona1.mostrar_detalle()
Persona.mostrar_detalle(persona1)
persona1.telefono = '123456789' # No se comparte con otros objetos
print(persona1.nombre)
persona1.nombre = 'Pedro'
print(persona1.nombre)