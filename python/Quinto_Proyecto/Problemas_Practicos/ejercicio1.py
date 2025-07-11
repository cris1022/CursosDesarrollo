'''Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio'''

def devolver_distintos(num1,num2,num3):
    suma= num1+num2+num3
    if suma>15:
        print(f"la suma de {num1}, {num2} y {num3} es {suma}, por lo tanto su numero mayor es {max(num1,num2,num3)}")
    elif suma<10:
        print(f"la suma de {num1}, {num2} y {num3} es {suma}, por lo tanto su numero menor es {min(num1,num2,num3)}")
    else:
        print(f"la suma de {num1}, {num2} y {num3} es {suma}, por lo tanto su numero intermedio es {sorted([num1,num2,num3])[1]}") 

print("Hola Porfavore ingresa 3 numeros entreros de 0 a 100")

num1= int(input("Ingrese el primer numero: "   ))
num2= int(input("Ingrese el segundo numero: "  ))
num3= int(input("Ingrese el tercer numero: "   ))   

devolver_distintos(num1,num2,num3)

