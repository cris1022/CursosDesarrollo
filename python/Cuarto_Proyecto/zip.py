nombres=["Marcos", "Laura", "Mónica", "Javier" ]
edades=[25, 30, 28, 35]
ciudades=["Madrid", "Barcelona", "Valencia", "Sevilla"]  
datos_combinados = list(zip(nombres, edades, ciudades))
print(datos_combinados)


for nombre, edad, ciudad in datos_combinados:
    print(f'Nombre: {nombre}, tiene una Edad de: {edad} y vive en la ciudad: {ciudad}')


'''
Práctica Zip 1
Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín

Utiliza la función zip, loops, y las siguientes listas 
de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]'''

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for pais, capital in zip(paises, capitales):
    print(f'La capital de {pais} es {capital}')


marcas=["Toyota", "Ford", "BMW", "Audi", "Volkswagen"]
productos=["Corolla", "Mustang", "X5", "A4", "Golf"]
for marca,producto in zip(marcas, productos):
    print(f'La marca {marca} tiene el producto {producto}')


'''Crea el zip con las traducciones los números del 1 al 5 en español,
 portugués e inglés (en el mismo orden), y convierte el objeto generado 
 en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]'''   

español=["uno", "dos", "tres", "cuatro", "cinco"]
portugues=["um", "dois", "três", "quatro", "cinco"]
ingles=["one", "two", "three", "four", "five"]
numeros=list(zip(español, portugues, ingles))
print(numeros)
