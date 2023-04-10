rc = int(input("Cantidad de respuestas correctas: "))
ri = int(input("Cantidad de respuestas incorrectas: "))
rb = int(input("Cantidad de respuestas en blanco: "))

resultado = int((rc*3) + (ri * -1))

print ("----------------------")

print ("Cantidad de respuestas en blanco: ", rb)
print ("Cantidad de respuestas incorrectas: ", ri)
print ("Cantidad de respuestas correctas ", rc)

print ("----------------------")

print ("Puntaje final: ", resultado)