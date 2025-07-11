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
def pedir_letras():
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

def mosntrar_nuevo_tablero(palabgra_elegida):   

  
