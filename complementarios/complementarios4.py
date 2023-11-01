'''
Construya un algoritmo que, dado una entrada n, calcule la
suma de los términos de una progresión aritmética como la
que se muestra a continuación: 10; 15; 20; 25; 30 .....Tn. Esto
es, su algoritmo debe calcular el valor: 10 + 15 + 20 + 25 + 30
+ ... + Tn.

'''


n = int(input("Ingrese el valor de n: "))


a = 10  
d = 5   
suma = (n / 2) * (2 * a + (n - 1) * d)


print("La suma de los primeros", n, "términos de la progresión es:", suma)