'''
Escribir un algoritmo que imprima los 10 primeros números
pares comenzando en 2 e imprima también sus respectivos
cubos. Por ejemplo: 2 – 8 ; 4 – 64; 6 – 216 ...

'''

numero = 2

for i in range(1, 11):
    cubo = numero ** 3
    print(numero, "-", cubo)
    numero += 2