'''Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y 
luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio'''

def describir_persona(name,**kwargs):
    print(f"El nombre de la persona es: {name} ")
    for key, value in kwargs.items():
        print (f"{key} = {value}")
        
nombre=input("Ingrese el nombre de la persona: ")
color_ojos= input("Ingrese el color de ojos: ")
color_pelo= input("Ingrese el color de pelo: ")

describir_persona(nombre, color_ojos=color_ojos, color_pelo=color_pelo)
