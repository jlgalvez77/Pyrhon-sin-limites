def listar_terminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")

listar_terminos(nombre='Jose', apellido='Galvez', edad=47)