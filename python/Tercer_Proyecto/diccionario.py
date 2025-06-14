diccionario={'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario['c1'])

cliente={'nombre':'Juan', 'apellido':'perez','peso':'88','talla':'1.80'}
consulta= cliente['nombre']

print (consulta)


dic={'c1':55,'c2':[10,15,20,25],'c3':{'s1':'100','s2':200},}

print(dic['c2'][0])


dic2={'c1':['a','b','c','d'],'c2':['e','f','g','h']}
print(dic2['c2'][0].upper())

#Agregaremos elementos 

dic2['c3']=['i']

print(dic2)