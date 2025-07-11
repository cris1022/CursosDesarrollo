# Función que suma números pasados como argumentos y muestra el resultado con el nombre
def sumar_numeros_personas(nombre, *args):
   
    total = 0
    for num in args:
        total += num
    print(f"{nombre}, la suma de tus números es: {total}")
    return total

    
    
nombre_usuario = input("Ingrese su nombre: ")
resultado2 = sumar_numeros_personas(nombre_usuario, 10, 20, 30)
