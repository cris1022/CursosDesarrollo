precios_cafe=[('capuccino', 1.50), ('espresso', 1.00), ('latte', 2.00), ('americano', 10.75)]
def precio_cafe_caro(nombre_cafe):
    precio_mayor=0
    precio_cafe_caro=''
    for cafe, precio in precios_cafe:
        if precio>precio_mayor:
            precio_mayor=precio
            precio_cafe_caro=cafe
        else:
            pass
    return (precio_cafe_caro, precio_mayor)

print(f"El café más caro es {precio_cafe_caro(precios_cafe)[0]} con un precio de {precio_cafe_caro(precios_cafe)[1]}")
