from random import *

aleatorio = randint(1,50)
print(f"El número aleatorio es: {aleatorio}")


aleatorio2=round(uniform(1,5),3)# un decimal aleatorio del 1 al 5 con 3 decimales 
print(f"El número aleatorio con decimales es: {aleatorio2}")


aleatorio3= round(random(),1)# un número aleatorio entre 0 y 1 con un decimal
print(f"El número aleatorio entre 0 y 1 es: {aleatorio3}")


colores=['rojo', 'verde', 'azul', 'amarillo', 'naranja']
aleatorio4= choice(colores) # elige un color aleatorio de la lista
print(f"El color aleatorio es: {aleatorio4}")

cartas=list(range(1,50,5)) # una lista del 1 al 50 de 5 en 5 
shuffle(cartas) # mezcla la lista
print(f"Las cartas mezcladas son: {cartas}")



'''
Práctica Random 1
Implementa la función randint() de la librería random que te permita obtener u
n número entero del 1 al 10, y almacena dicho valor en una variable llamada 
aleatorio'''
from random import *

aleatorio=randint(1,10)

print(f'tu numero aleatorio es {aleatorio}')

'''
Práctica Random 2
Implementa la función random() de la librería random que te permita obtener
 un número decimal entre 0 y 1, y almacena dicho valor en una variable 
 llamada aleatorio'''


aleatorio3= round(random(),1)# un número aleatorio entre 0 y 1 con un decimal
print(f"El número aleatorio entre 0 y 1 es: {aleatorio3}")

aleatorio3= round(random(),1)# un número aleatorio entre 0 y 1 con un decimal
print(f"El número aleatorio entre 0 y 1 es: {aleatorio3}")


'''Práctica Random 3
Utiliza el método choice() de la librería random
para obtener un elemento al azar de la lista de nombres a 
continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]'''


nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo=choice(nombres)
print(f'El nombre escogido al azar es {sorteo}')
