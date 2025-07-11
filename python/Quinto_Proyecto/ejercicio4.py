
def numero_primo(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    
def contar_primos(num1):
    """
    Muestra todos los números primos desde 0 hasta num1 (incluido) 
    y devuelve la cantidad encontrada.
    Args:
        num1 (int): límite superior del rango
    Returns:
        int: cantidad de números primos encontrados
    """
    contador = 0
    print("Números primos encontrados:")
    
    for i in range(2, num1 + 1):  # Empezamos desde 2 (primer primo)
        if numero_primo(i):
            contador += 1
            print(i)  # Solo muestra el número primo, sin True/False
    
    return contador  # Devuelve la cantidad encontrada

# Ejemplo de uso:
numero = int(input("Ingrese un numero entero positivo: "))
print(f"Buscando números primos desde 0 hasta {numero}:")
total_primos = contar_primos(numero)
print(f"\nCantidad total de números primos encontrados: {total_primos}")
      

