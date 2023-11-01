'''
Crear un algoritmo, que dado N números enteros ingresados
por teclado determine cuál de ellos es el menor y mayor
respectivamente.

'''

N = int(input("Ingrese la cantidad de números: "))

numeros = []
for i in range(N):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

menor = numeros[0]
mayor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > mayor:
        mayor = numero

print("El menor número es:", menor)
print("El mayor número es:", mayor)