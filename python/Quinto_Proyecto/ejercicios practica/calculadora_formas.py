'''Ejercicio 1: Calculadora de Área de Formas
Crea una función llamada calcular_area que, sin 
recibir argumentos, pida al usuario el tipo de forma 
(círculo, cuadrado o triángulo) y sus dimensiones necesarias. 
Luego, esta función debe llamar internamente a otra función 
(por ejemplo, area_circulo, area_cuadrado, area_triangulo) 
para calcular y retornar el área. La función principal calcular_area
 debe retornar un mensaje que incluya el área calculada o un mensaje 
 de error si la forma no es reconocida.'''

import math
def area_circulo(radio):
    '''Calcula el área de un círculo dado su radio'''
    return math.pi * (radio ** 2)
def area_triangulo(base,altura):
    return(base * altura) / 2

def area_cuadrado(lado):
    '''Calcula el área de un cuadrado dado su lado'''
    return lado ** 2

def area_forma():
    forma= input("Ingrese la forma que desea evaluar (circulo, cuadrado o triangulo): ").lower()
    if forma=="circulo":
        radio=float(input("Ingrese el radio del círculo: "))
        area= area_circulo(radio)
        return print(f"El área del círculo es: {area:.2f}")
    elif forma=="cuadrado":
        lado=float(input("Ingrese el lado del cuadrado: "))
        area= area_cuadrado(lado)
        return print(f"El área del cuadrado es: {area:.2f}")
    elif forma=="triangulo":
        base=float(input("Ingrese la base del triángulo: "))
        altura=float(input("Ingrese la altura del triángulo: "))
        area= area_triangulo(base, altura)
        return print(f"El área del triángulo es: {area:.2f}")
    else:
        return print("Forma no reconocida.")

# Llamada a la función para calcular el área de la forma
area_forma()
