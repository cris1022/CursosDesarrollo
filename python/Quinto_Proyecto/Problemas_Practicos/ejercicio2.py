'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']'''

def letras_unicas_ordenadas(palabra):
    # Convertimos la palabra a un conjunto para eliminar duplicados
    letras_unicas = set(palabra)
    
    # Convertimos el conjunto a una lista y la ordenamos alfabéticamente
    letras_ordenadas = sorted(letras_unicas)
    return print(f"La palabra '{palabra}' tiene las siguientes letras únicas en orden alfabético: {letras_ordenadas}")

    
    

palabra= input("Introduce una palabra: ")
letras_unicas_ordenadas(palabra)

