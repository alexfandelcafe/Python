pe =int(input("Cantidad de partidos empatados: "))
pg =int(input("Cantidad de partidos ganados: "))
pp =int(input("Cantidad de partidos perdidos: "))

resultado = int((pg * 3) + (pe * 1))

print ("----------------------")

print ("Cantidad de partidos ganados: ", pg)
print ("Cantidad de partidos empatados : ", pe)
print ("Cantidad de partidos perdidos ", pp)

print ("----------------------")

print ("Puntaje final: ", resultado)