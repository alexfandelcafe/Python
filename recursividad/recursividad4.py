'''
inicializamos cont a 0.

comenzamos un bucle desde i = 1 hasta limite = 456871

oara cada valor de i, comprobamos si es primo 

para i = 1, 2, 3, 4, 5, y 6, primo se establece en True porque son primos
para i = 7, primo se establece en true porque 7 es primo
para i = 8, primo se establece en false porque 8 no es primo

el proceso continúa para otros valores de i
Luego, para cada número primo encontrado se muestra en la salida

al final, se muestra el total de números primos encontrados en el rango

'''


primer_numero = 1
limite = 456871
cont = 0

for i in range(primer_numero, limite + 1):
    primo = True
    j = 2
    while j < i and primo:
        if i % j == 0:
            primo = False
        else:
            j += 1
    if primo:
        print(i, "es primo")
        cont += 1

print("Entre", primer_numero, "y", limite, "hay", cont, "números primos.")