def suma(**kwargs):
    
    total=0
    for key, value, in kwargs.items():
        print(f"{key} = {value}")
        total += value  
    return total

print(suma(a=1, b=2, c=3, d=4, e=5))  # Imprime: 15 


def prueba(num1,num2,*args, **kwargs):

    print(f"el primer numero es: {num1}")
    print(f"el segundo numero es: {num2}")
    for arg in args:
        print(f"Argumento adicional: {arg}")

    for key, value in kwargs.items():
        print(f"{key} = {value}")

numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))  
argumentos_adicionales = input("Ingrese argumentos adicionales separados por comas: ").split(',')
kgwards_adiciones= input("Ingrese kwarg adicionales en formato clave=valor separados por comas: ").split(',')
prueba(numero1,numero2,argumentos_adicionales,kgwards_adiciones)


    
   