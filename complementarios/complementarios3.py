'''
Escribir un algoritmo que imprima los 10 primeros números
primos comenzando en 2 e imprima también sus respectivos
cubos.

'''

def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

numero = 2
contador_primos = 0

while contador_primos < 10:
    if es_primo(numero):
        cubo = numero ** 3
        print("Número primo:", numero, "Cubo:", cubo)
        contador_primos += 1
    numero += 1