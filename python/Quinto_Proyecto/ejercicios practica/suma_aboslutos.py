def sumar_valores_aboslutos(*args):
    total=0
    for num  in args:
        total+=abs(num)
    return total
print (sumar_valores_aboslutos(-4, 5, -3))  # Salida: 12
print (sumar_valores_aboslutos(-4, -5, -3)) # Salida: 12            