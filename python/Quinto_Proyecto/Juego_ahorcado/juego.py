from random import choice
# las palabras al azar 

palabras=['panadero', 'gato', 'perro', 'raton', 'elefante', 'jirafa', 'tigre', 'leon', 'cocodrilo', 'serpiente']
# Lista de la letras correctas e incorrrectas 
letras_correctas=[]
letras_incorrectas=[]
intentos=6
acierto=0
juego_terminado=False

#Funcion para elegir palabra al azar 
def elegir_palabra(lista_palabras):
    palabra_elegida= choice(lista_palabras)
    letras_unicas=len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

#Letra Elegida por el usuario
def pedir_letra():
    letra_elegida=''
    es_valida=False
    abecedario='abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida=input('Elige ujna letra:').lower()
        if len(letra_elegida)==1 and letra_elegida in abecedario:
            es_valida=True
        else:
            print('Debes ingresar una sola letra del abecedario')
    return letra_elegida

def mostrar_nuevo_tablero(palabgra_elegida):
    lista_oculta=[]
    for letra in palabgra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))
    

#funcion para chequear si la letra elegida esta en la palabra
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin= False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias+=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has elegido esa letra')    
    else:
        letras_incorrectas.append(letra_elegida)
        vidas-=1
    if vidas==0:
        fin= perder()
    elif coincidencias==letras_unicas:
        fin=ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print(f"La palabra era: {palabra}")
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print(f"Felicidades, has descubierto la palabra: {palabra_descubierta}")
    return True

def reiniciar_juego():
    """
    Reinicia todas las variables del juego para una nueva partida
    """
    global letras_correctas, letras_incorrectas, intentos, acierto, juego_terminado
    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    acierto = 0
    juego_terminado = False

def jugar_de_nuevo():
    """
    Pregunta al usuario si quiere jugar otra vez
    """
    while True:
        respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor, responde 's' para sí o 'n' para no.")

# Bucle principal del juego
continuar_jugando = True

while continuar_jugando:
    # Reiniciar juego para nueva partida
    reiniciar_juego()
    
    # inicio del Juego
    # Elegir una palabra al azar        
    palabra, letras_unicas = elegir_palabra(palabras)    
    
    print("\n¡Bienvenido al juego del Ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra.")
    
    # Bucle de una partida
    while not juego_terminado:
        print('\n' + '*' * 20 + '\n')
        mostrar_nuevo_tablero(palabra)
        print('\n') 
        print('Letras incorrectas: '+ ' - '.join(letras_incorrectas))  
        print(f'Intentos restantes: {intentos}')
        print('\n' + '*' * 20 + '\n')
        letra=pedir_letra()

        intentos,terminado, acierto = chequear_letra(letra, palabra, intentos, acierto)

        juego_terminado=terminado
    
    # Preguntar si quiere jugar de nuevo
    continuar_jugando = jugar_de_nuevo()

print("\n¡Gracias por jugar al Ahorcado! ¡Hasta la próxima!")


