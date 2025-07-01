from random import *
intentos=0
numero_secreto=randint(1,100)   
nombre_usuario=input("Ingresa tu nombre: ")
print (f'Hola {nombre_usuario}, he pensado un número del 1 al 100, ¿puedes adivinarlo? \n Tienes 8 intentos ')

while intentos<8:
    numero_usuario= int(input("Ingresa un numero:"))
    intentos+=1

    if numero_usuario==numero_secreto:
        print(f"¡Felicidades {nombre_usuario}! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
        break
    elif numero_usuario<numero_secreto:
        print(f"El número secreto es mayor que {numero_usuario}. Te quedan {8-intentos} intentos.")
    else:
        print(f"El número secreto es menor que {numero_usuario}. Te quedan {8-intentos} intentos.") 

if intentos==8:
    print(f"Lo siento {nombre_usuario}, no adivinaste el número secreto {numero_secreto} en 8 intentos. ¡Inténtalo de nuevo!")



