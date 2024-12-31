def listar_nombres(*args):
    for nombre in args:
        print(f"Hola {nombre}")

listar_nombres('Jose', 'Maria', 'Pedro', 'Ana')