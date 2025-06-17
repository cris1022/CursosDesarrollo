# Analizador de texto 

texto=(input("Ingresa un texto a eleccion: "))
letras=[]

#Transaformacion a minusculas
texto=texto.lower()

letras.append(input("Ingresa la primera letra:").lower())

letras.append(input("Ingresa la segunda letra:").lower())

letras.append(input("Ingresa la tercera letra:").lower())

print("\n")
print("CANTIDAD DE LETRAS")

cantidad_letras1= texto.count(letras[0])

cantidad_letras2= texto.count(letras[1])

cantidad_letras3= texto.count(letras[2])



print(f"Hemos encontrado la letra '{letras[0]}' repetida{ cantidad_letras1} veces en el texto.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces en el texto.")    
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces en el texto.")


print("\n")
print("CANTIDAD DE PALABRAS")


palabras=texto.split()
print(f"hemos encntrado {len(palabras)} palabras en el texto.")




print("\n")
print("LETRAS DE INICIO Y DE FIN ")


letra_inicio=texto[0]
letra_fin=texto[-1]

print(f"hemos encntrado la letra de inicio la cual es  {letra_inicio} y la letra de fin la cual es {letra_fin}.")


print("\n")
print("TEXTO INVERTIDO ")

palabras.reverse()
texto_invertido=" ".join(palabras)
print(f"El texto invertido es: {texto_invertido}.")
print("\n") 


print("\n")
print("USCANDO LA PALABRA PYTHON ")

palabras.reverse()
buscar_python="python" in texto
dic={True:"si", False:"no"}
print(f"¿La palabra 'python' se encuentra en el texto? {buscar_python}.")
si = "Si"
no = "No"   