def cantidad_atributos(**kwargs):
    """
    Cuenta la cantidad de parámetros que se entregan como kwargs.
    Returns:
        int: cantidad de parámetros recibidos
    """
    return len(kwargs)
cantidad_atributos()  # Devuelve: 0
cantidad_atributos(nombre="Juan", edad=25, ciudad="Madrid")  # Devuelve: 3
cantidad_atributos(a=1, b=2, c=3, d=4, e=5)  # Devuelve: 5

print(cantidad_atributos(nombre="Juan", edad=25, ciudad="Madrid"))  # Imprime: 3