'''
Dado que el valor de e
x
se puede calcular por aproximación

de la siguiente suma:
e = 1 + x+x2
/2! + x3
/3! + ..... + xn
/n!

Realizar el algoritmo (Diagrama de flujo) que tome un valor
para X y calcule e
x
hasta que xn

/n! (error o aproximación) sea

menor a 0.00001

(no lo entendi se me dan mal las matematicas :( )

'''



x = float(input("Ingrese el valor de x: "))

e_x = 1.0  
termino = 1.0
n = 1

while termino >= 0.00001:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    termino = (x**n) / factorial #llegue a esta conclucion
    e_x += termino
    n += 1

print("e^x =", e_x)