class Aritmetica:
    '''
    Clase Aritmetica para realizar las operaciones de suma, resta, multiplicacion y division
    '''
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
# Instanciar la clase
aritmetica = Aritmetica(5, 3)
print(f'Suma: {aritmetica.sumar()}')
print(f'Resta: {aritmetica.restar()}')
print(f'Multiplicacion: {aritmetica.multiplicar()}')
print(f'Division: {aritmetica.dividir():.2f}')