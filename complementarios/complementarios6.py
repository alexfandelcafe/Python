'''
Escribir un algoritmo que invierta los dígitos de un número
positivo entero. Usar operadores módulo y división para ir
obteniendo los dígitos uno a uno. Por ejemplo, si se ingresa
37368 debe retornar el numero 86373

'''

numero = int(input("Ingrese un número entero positivo: "))

numero_invertido = 0
factor = 10

while numero > 0:
    digito = numero % 10 
    numero_invertido = numero_invertido * factor + digito
    numero = numero // 10  

print("El número invertido es:", numero_invertido)