'''Ejercicio 2: Conversor de Temperaturas
Diseña una función obtener_temperatura que pida 
al usuario un valor numérico y la unidad 
('C' para Celsius, 'F' para Fahrenheit). 
Esta función debe retornar ambos valores. 
Luego, crea una segunda función convertir_temperatura 
que reciba estos dos valores y retorne la temperatura 
convertida a la otra unidad, o un mensaje de error si la 
unidad no es válida. (Fórmula: C=(F−32)∗5/9; F=C∗9/5+32).'''

# Función que convierte grados Fahrenheit a Celsius
def grados_celsius(fahrenheit):
    '''Convierte grados Fahrenheit a Celsius'''
    return (fahrenheit - 32) * 5 / 9

# Función que convierte grados Celsius a Fahrenheit
def grados_fahrenheit(celsius):
    '''Convierte grados Celsius a Fahrenheit'''
    return celsius * 9 / 5 + 32

# Función que pide al usuario el valor y la unidad de temperatura
def obtener_temperatura():
    """
    Pide al usuario un valor numérico y la unidad de temperatura.
    Returns:
        tuple: (temperatura, unidad) - valor numérico y unidad ingresada
    """
    temperatura = float(input("Ingrese la temperatura: "))
    medida = input("Ingrese la unidad de medida (C para Celsius, F para Fahrenheit): ").upper()
    return temperatura, medida

# Función que convierte la temperatura según los valores recibidos
def convertir_temperatura(temperatura, unidad):
    """
    Convierte la temperatura a la otra unidad o retorna mensaje de error.
    Args:
        temperatura (float): valor de la temperatura
        unidad (str): unidad original ('C' o 'F')
    Returns:
        str: mensaje con la temperatura convertida o error
    """
    if unidad == "C":
        fahrenheit = grados_fahrenheit(temperatura)
        return f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F"
    elif unidad == "F":
        celsius = grados_celsius(temperatura)
        return f"La temperatura en grados Celsius es: {celsius:.2f}°C"
    else:
        return "Unidad de medida no válida. Por favor, ingrese 'C' o 'F'."

# Ejemplo de uso siguiendo el diseño del ejercicio
if __name__ == "__main__":
    temp, unidad = obtener_temperatura()
    resultado = convertir_temperatura(temp, unidad)
    print(resultado)
