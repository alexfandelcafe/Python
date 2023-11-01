'''
Dado el siguiente Pseudocódigo determine cuál es el valor y
el rango del primer término que supere el valor 300

Algoritmo serie
Var

Al, A2, an, cont: entero
inicio

A1=1

A2=0

An = Al +(2* A2)

Mientras
A2=Al
Al=an
an = A1+(2* A?)
cont = cont+1
Finmientras

Escribir (“El rango es “, cont.” y el resultado es”, an)
fin

'''



A1 = 1
A2 = 0
An = A1 + (2 * A2)
cont = 0


while An <= 300:
    A2 = A1
    A1 = An
    An = A1 + (2 * A2)
    cont += 1

print("El rango es", cont, " y el resultado es ",An)

