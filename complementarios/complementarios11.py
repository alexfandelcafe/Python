'''
Ingresar por teclado 100 números enteros y calcular cuántos
de ellos son pares. Se imprime el resultado.

'''

contador_pares = 0

for i in range(1, 101):
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 2 == 0:
        contador_pares += 1

print("De los 100 números ingresados, ", contador_pares, "son pares.")