def verificar_3_cifras (numero):
    return numero in range(100,1000)

resulado=verificar_3_cifras(123)
print(resulado)

suma= 1+56
resultado=verificar_3_cifras(suma)
print(resultado)
# verificar elemento de una lista 

def verificar_3_cifras_lista (lista):
    for n in range (100,1000):
        if n in lista:
            print(f"El número {n} está en la lista.")
            return True
        else:
            pass
lista3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,200]
resultado_lista = verificar_3_cifras_lista(lista3)
print(resultado_lista)  


#verificar en un lista los numeros positivos 
def verificar_positivo(lista_numeros):
    for numero in lista_numeros:
        if numero>0:
            print(f"El nummero {numero} esta en la lista y es positivo")
            return True
        else:
            pass
lista_numeros = [-1, -2, -3, -4, -5, -6]
resultado_positivo = verificar_positivo(lista_numeros)
print(resultado_positivo)

#Suma de numero menores a 1000
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero >0 and numero <1000:
            suma+=numero
    return suma
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1011, 1121, 1298, 138, 1400, 1500, 16, 1700, 1800, 1900, 2000]
resultado_suma = suma_menores(lista_numeros)
print(f"La suma de los números menores a 1000 es: {resultado_suma}")


#Contar la cantidad de pares en la lista 
def cantidad_pares(lista_numeros):
    contador=0
    for numero in lista_numeros:
        if numero%2==0:
            contador+=1
    return contador
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,]
resultado_pares = cantidad_pares(lista_numeros)
print(f"La cantidad de números pares en la lista es: {resultado_pares} ")    