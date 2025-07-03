def multiplicar(num1, num2):
    '''Función que multiplica dos números'''
    print("El resultado de la multiplicación es:", num1 * num2)

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
multiplicar(numero1, numero2)

'''Crea una función llamada potencia que tome dos 
valores numéricos como argumentos. Deberá devolver 
el número que resulte de resolver una potencia, 
utilizando el primer número como base, y el segundo 
como exponente:'''

def potencia(base, exponente):
    ''' Funcion que calcula la potencia de u número'''
    resultado= base**exponente
    print (f"El resultado de {base} elvado a la {exponente} es {resultado}")

base_usuario=int(input("Ingrese la base: "))
exponente_usuario=int(input("Ingrese el exponente: "))
potencia(base_usuario, exponente_usuario)


'''Práctica Return 2
Crea una función llamada usd_a_eur que tome como único 
parámetro un valor numérico (un monto en dólares estadounidenses)
, y devuelva como resultado el monto equivalente en euros. 
A fines de este ejemplo, tomaremos la conversión 
1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un 
monto cualquiera para entregárselo a tu función y evaluar 
su resultado.

Pista: para realizar la conversión, la función internamente 
debe multiplicar este valor en dólares por 0.90 para obtener 
el monto equivalente en euros.'''

def usd_a_eur(dolares):
    '''Función que convierte dólares a euros'''
    tasa_cambio = 0.90
    euros = dolares * tasa_cambio
    return euros

dolares = float(input("Ingrese el monto en dólares: "))
euros = usd_a_eur(dolares)
print(f"El monto en euros es: {euros}")


def invertir_palabra(palabra):
    '''Función que invierte una palabra'''
    resultado =palabra[::-1]
    print (f"la palabra :{palabra} invertida es {resultado}")
palabra_usuario = input("Ingrese una palabra")

invertir_palabra ( palabra_usuario ) 
