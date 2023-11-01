'''
Escriba un algoritmo tal que dado como datos X números
enteros, obtenga el número de ceros que hay entre estos
números. Por ejemplo, si se ingresa 6 datos: 9 0 4 8 0 1
El algoritmo arroja que hay 2 ceros.

'''

n = int(input("Ingrese la cantidad de números: "))

contador_ceros = 0

for i in range(n):
    numero = int(input("Ingrese un número entero: "))
    if numero == 0:
        contador_ceros += 1

print("Hay", contador_ceros, "ceros entre los números ingresados.")