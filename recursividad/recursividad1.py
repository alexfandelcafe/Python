'''
Se coloca un capital C, a un interés I (que oscila entre 0 y
100), durante M años y se desea saber en cuanto se habrá
convertido ese capital en “M” años, sabiendo que es
acumulativo.

(Tuve que buscar en internet como hacer comentarios de varias lineas)

(hecho en clase terminado en casa)

'''


C = 0.0
I = 0.0
M = 0
j = 0


while C <= 0 or I < 0 or I > 100 or M <= 0:
    print("Introduce el capital, el interés y el tiempo apropiados")
    C = float(input("Capital (C): "))
    I = float(input("Interés anual (0-100) (I): "))
    M = int(input("Tiempo en años (M): "))


for j in range(1, M + 1):
    C = C + (C * I / 100)

print("Después de", M, "años, tendrás", C, "soles")