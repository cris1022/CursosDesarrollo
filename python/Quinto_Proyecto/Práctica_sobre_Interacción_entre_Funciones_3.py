from random import *

from random import choice

def lanzar_moneda():
    return choice(['Cara', 'Cruz'])

def probar_suerte(lista):
    caras = 0
    for intento in range(1, 4):
        resultado = lanzar_moneda()
        print(f"Intento {intento}: {resultado}")
        if resultado == 'Cara':
            caras += 1
        if caras == 2:
            print("¡Conseguiste 2 caras! La lista fue salvada.")
            return lista
    print("No conseguiste 2 caras en 3 intentos. La lista se autodestruirá.")
    return []

# Ejemplo de uso:
lista_numeros = [1, 2, 3, 4, 5]
nueva_lista = probar_suerte(lista_numeros)
print("Lista final:", nueva_lista)