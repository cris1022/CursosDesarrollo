'''Crea una función llamada reducir_lista() que tome una lista como 
argumento (crea también la variable lista_numeros), y devuelva la 
misma lista, pero eliminando duplicados 
(dejando uno solo de los números si hay repetidos) y eliminando el 
valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver
 [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento
 la lista devuelta por la anterior función, y que calcule el promedio 
 de los valores de la misma. Debe devolver el resultado, 
 sin imprimirlo.'''

lista_numeros = [15, 2, 7, 1, 2, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def reducir_lista(lista):
    lista_sin_duplicados=list(set(lista))  # Elimina duplicados
    elimanar_mayor=max(lista_sin_duplicados)  # Encuentra el valor más alto
    lista_sin_duplicados.remove(elimanar_mayor)  # Elimina
    return lista_sin_duplicados  # Devuelve la lista sin duplicados y sin el valor más alto

def promedio(lista):
    if len(lista)>=2:
        return sum(lista)/len(lista)
    else:
        return "La lista debe tener más de 1 elementos para calcular el promedio."
    
# Reducir la lista original
lista_reducida = reducir_lista(lista_numeros)

# Calcular el promedio de la lista reducida
resultado_promedio = promedio(lista_reducida)

# Mostrar los resultados
print("Lista reducida:", lista_reducida)
print("Promedio:", resultado_promedio)