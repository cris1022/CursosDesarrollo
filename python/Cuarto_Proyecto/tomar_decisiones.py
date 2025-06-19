if 10>9:
    print("10 es mayor que 9 es lo correcto ")


if 5==2:
    print("CORRECTO")
else:
    print("INCORRECTO")

mascota= input('ingresa el tipo de mascota que tienes: ').lower()

if mascota =='gato':
    print('tienes un gato ')    
elif mascota == 'perro':
    print('tienes un perro ')
elif mascota == 'pez':
    print('tienes un pez ')   
else:
    print('nos se que animaL tienes  ')



edad= int(input('ingresa la edad  que tienes: '))

if edad >=18:
    print('Eres mayor de edad  ')    
elif edad  < 18 and edad >=12:
    print('eres un adolcente  ')
elif edad < 12:
    print('eres un niño ')
else:
    print('nos se que edad tienes  ')



habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python:
    print("Para postularte, necesitas saber programar en Python")



