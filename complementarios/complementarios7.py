'''
Ingresar un número y determinar si es número PRIMO.

'''

numero = int(input("Ingrese un número: "))

if numero <= 1:
    es_primo = False
elif numero == 2:
    es_primo = True
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")