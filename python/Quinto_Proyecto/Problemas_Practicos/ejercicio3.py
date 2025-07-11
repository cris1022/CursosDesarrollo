'''Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False'''

def cero_dos_veces_consecutivo(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            print(f"Se encontraron dos ceros consecutivos en la secuencia: {args[i]}, {args[i + 1]}")
            print("Resultado: True")
            return True
        else:
            print(f"No se encontraron dos ceros consecutivos en la secuencia: {args[i]}, {args[i + 1]}")
    print("Resultado: False")
    return False

# ✅ Entrada y conversión correcta
entrada = input("Ingrese una secuencia de números separados por comas: ")
valores = [int(x.strip()) for x in entrada.split(',')]

# ✅ Llamar la función desempaquetando la lista
cero_dos_veces_consecutivo(*valores)






                    
    
    
            