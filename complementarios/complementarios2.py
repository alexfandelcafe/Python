'''
Escribir un algoritmo que imprima los 10 primeros números
pares comenzando en 2 e imprima también sus respectivos
cubos.

'''

numero = 2

for i in range(1, 11):
    cubo = numero ** 3
    print("Número par:", numero, "Cubo:", cubo)
    numero += 2