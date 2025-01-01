def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input('Introduce la temperatura en Celsius: '))
fahreheit = float(input('Introduce la temperatura en Fahrenheit: '))
print(f'{celsius} grados Celsius son {celsius_a_fahrenheit(celsius)} grados Fahrenheit')
print(f'{fahreheit} grados Fahrenheit son {fahrenheit_a_celsius(fahreheit)} grados Celsius')

