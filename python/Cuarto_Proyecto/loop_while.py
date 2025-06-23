monedas=0

while monedas<=100:
    if monedas %2==0:
        print(f"Monedas: {monedas} - es Par")
    else:
        print(f"Monedas: {monedas} - es Impar")
    monedas+=1

respuesta='s'
while respuesta=='s':
    respuesta=input("Desea continuar? (s/n): ").lower()
else:
    print("Gracias por participar")
    print("Fin del programa")
    print("Hasta luego") 

# PASS SALTA UNA ACION, BREAK LA TERMINA Y CONTINUE SALTA A LA SIGUIENTE ITERACION  
# 
nombres=input("Ingrese un nombre: ")
for letra in nombres:
    if letra=='a':
        continue
    print(letra)


nombres2=input("Ingrese un nombre: ")
for letra in nombres2:
    if letra=='a':
        break
    print(letra) 

'''
Práctica Loop While 1
Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.'''   

numero=10
while numero >= 0:
    print(numero)
    numero -= 1

'''Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).''' 


numero = 50

while numero >=0:
    if numero %5==0:
        print(f"el {numero} ves divisible por 5")
       
    numero-=1


'''
Práctica Interrupción de Flujo
Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

'''    


lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero <0:
        break
    print (numero)
        
