from random import shuffle
# lista inicial

palitos= ['-','--','---','----']


# mesclar palitos usamos shuffle de random

def mezclar_palitos(lista):
    shuffle(lista)
    return lista


# pedirle intento
def pedir_intento():
    intento= ''
    while intento not in ['1','2','3','4']:
        intento= input('Elige un palito (1, 2, 3 o 4): ')
        if intento not in ['1','2','3','4']:
            print('Por favor, elige un número válido.')
    return intento




# compronbar intento 

def comprobar_intento(lista, intento):
    if lista[intento-1] == '-':
        print('¡a lavar los palatos!')
    else:
        print('¡te haz salvado !')

    print(f"te ha tocado {lista[intento-1]} palito")

palitos_mezclados = mezclar_palitos(palitos)
selccion = pedir_intento()
comprobar_intento(palitos_mezclados, int(selccion))