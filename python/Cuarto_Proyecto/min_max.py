menor=min(58,96,74,35,1)
mayor=max(58,96,74,35,1)
print(f'El número menor es: {menor} y el número mayor es: {mayor}')

nombres=["Marcos", "laura", "Mónica", "Javier"]
print(f'El primer nombre alfabeticamemenbte ordenado es {min(nombres).lower()} y el último es {max(nombres).lower()}    ')

'''Obtén el valor máximo entre los valores de la siguiente lista, 
y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 1
21676, 6654067, 353254, 123134, 55**12, 611**5] '''

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(f'El valor maximo es {valor_maximo}    ')


'''
Práctica Min y Max 2
Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista 
de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 
6654067, 353254, 123134, 552512, 611665]'''

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

# Corrección de la f-string para un mejor formato multilínea
print(f'El rango corresponde a la diferencia entre el valor máximo, el cual es {max(lista_numeros)} \n'
      f'y el valor mínimo que es {min(lista_numeros)}, y su resultado es {rango}.')




diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades)

print(f'la edad minima es {edad_minima} y su nombre es {list(diccionario_edades.keys())[list(diccionario_edades.values()).index(edad_minima)]}. \n'
      f'El último nombre en orden alfabético es {ultimo_nombre} y su edad es {diccionario_edades[ultimo_nombre]}.')