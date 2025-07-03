def saludar_persona(nombre):
    '''Función que saluda a una persona '''
    print("Hola"+ " " + nombre + "!")

saludar_persona('Crisian Abondano')   
saludar_persona('Jose')     

'''Práctica Crear Funciones 1
Declara una función llamada saludar, que cada vez que sea llamada 
imprima en pantalla "¡Hola mundo!"

Solo debes definir la función, no debes invocarla luego.'''

def saludar():
    '''Función que saluda al mundo'''
    print("¡Hola mundo!")
saludar()


nombre2= input("Ingrese su nombre: ")
def saludar_persona2(nombre):
    '''Función que saluda a una persona '''
    print("Hola" + " " + nombre + "!")

saludar_persona2(nombre2)   


def bienvenida_persona(nombre):
    '''Función que da la bienvenida a una persona '''
    print("Bienvenido" + " " + nombre + "!")

bienvenida_persona('')


'''Declara una función llamada cuadrado, que tome 
como argumento un número cualquiera, y que cada vez 
que sea llamada, imprima en pantalla el cuadrado de 
dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función 
es un_numero. Crea dicha variable y asígnale un número 
cualquiera.'''

numero_usario = int(input("Ingrese un número: "))
def cuadrado(un_numero):
    '''Función que calcula el cuadrado de un número'''
    resultado = un_numero ** 2
    print("El cuadrado de", un_numero, "es", resultado)

cuadrado(numero_usario)
