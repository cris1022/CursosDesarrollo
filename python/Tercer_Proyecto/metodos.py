texto="Este es un texto de Cristian"
resultado=texto.upper()
print(resultado)


texto2="Este es un texto de Cristian"
resultado=texto2[2].upper()
print(resultado)


#minusculas lower

texto3="Este es el texto de cristian t"
resultado=texto3.split("t")
print(resultado)


#el join separa lo elementos dentro del parentesis
resultado=texto3.split("t")
print(resultado)

a="aprender"
b="python"
c="es"
d="genial"
resultado=" ".join([a,b,c,d])

print (resultado)


resultado=texto3.find("cristian")
print(resultado)

#repalce texto.replacer("e","x")