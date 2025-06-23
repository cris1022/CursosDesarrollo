nombres=['Juan', 'Maria', 'Pedro', 'Luisa']

for nombre in nombres:
    print("Hola " + nombre)

lista_letras = ['a', 'b', 'c', 'd', 'e']
for letra in   lista_letras:
    indice_letra= lista_letras.index(letra)
    print(f"La letra {letra} se encuentra en el índice {indice_letra}")


nombres2= ['Ana', 'Luis', 'Carlos', 'Marta', 'Lupita', 'Laura']
for i in nombres2:
    if i.startswith('L'):
        print(f"{i} empieza con L")


numeros = [1, 2, 3, 4, 5]
mi_valor=0
for num in numeros:
    mi_valor=mi_valor+num
    print(mi_valor)

print(mi_valor)


palabra= 'python es gebial'
for letra in palabra:
    print(letra)

#iterar una lista de objetos
for a,b  in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#interar en un diccionario 

dic={'clave1':'a', 'clave2':'b', 'clave3':'c'}
for clave, valor in dic.items():
    print(f"La clave es {clave} y el valor es {valor}")


#    suma pares e imapres 

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numeros in lista_numeros:
    if numeros %2 ==0:
        suma_pares =suma_pares+numeros
    else:
        suma_impares=suma_impares+numeros
print(f"la suma de los pares es {suma_pares}")
print(f"la suma de los impares es {suma_impares}")

