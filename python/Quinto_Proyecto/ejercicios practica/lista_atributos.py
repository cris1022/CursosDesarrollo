def lista_atributos(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} = {value}")

kwargs_adiciones= input("Ingrese kwarg adicionales en formato clave=valor separados por comas: ").split(',')
lista_atributos(**dict(item.split('=') for item in kwargs_adiciones))