'''
Se coloca un capital C, a un interés I (que oscila entre 0 y
100), durante M años y se desea saber en cuanto se habrá
convertido ese capital en “M” años, sabiendo que es
acumulativo.

(hecho en clase terminado en casa)

'''

Numero = 0
i = 0
suma = 0


print("Introduce un número, y para acabar uno negativo")
Numero = int(input("Número: "))

while Numero > 0:
    suma = 0
    
    for i in range(1, Numero // 2 + 1):
        if Numero % i == 0:
            suma += i
    
    suma += Numero
    print("La suma de los divisores del número es", suma)
    
    Numero = int(input("Número: "))