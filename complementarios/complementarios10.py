'''
Ingresar 50 caracteres e indicar cuantas veces se repite el
carácter ‘a’.

'''

cadena = input("Ingrese una cadena de 50 caracteres: ")

contador_a = 0

for caracter in cadena:
    if caracter == 'a':
        contador_a += 1

print("El carácter 'a' se repite", contador_a, "veces en la cadena.")
