from random import *
palabras=["python", "programacion", "computadora", "algoritmo","funcion", "variable"]
palabra_secreta=choice(palabras)
letras_adivinadas=[]
intentos=0
print("¡Bienvenido al juego del Ahorcado!")
print("Adivina la palabra secreta. Tienes 6 intentos.") 
while intentos <6:
    print("\nPalabra:", " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]))
    letra_usuario = input("Ingresa una letra: ").lower()
    
    if len(letra_usuario) != 1 or not letra_usuario.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue
    
    if letra_usuario in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue
    
    letras_adivinadas.append(letra_usuario)
    
    if letra_usuario in palabra_secreta:
        print(f"¡Bien hecho! La letra '{letra_usuario}' está en la palabra.")
    else:
        intentos += 1
        print(f"Lo siento, la letra '{letra_usuario}' no está en la palabra. Te quedan {6 - intentos} intentos.")
    
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print(f"¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
        break
else:
    print(f"Lo siento, has agotado tus intentos. La palabra secreta era: {palabra_secreta}")
