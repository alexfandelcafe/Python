
'''
¿Cuáles y cuántos son los números primos comprendidos
entre 1 y 1000?

Inicio
    Cont <- 0
    Desde i=1 hasta 1000
      primo <- Verdadero
      j <- 2
      Mientras (i > j) y (primo = Verdadero)
        Si (i mod j = 0) entonces
          primo <- Falso
        Sino
          j <- j + 1
        Fin Si
      Fin Mientras
      Si primo = Verdadero entonces
        Escribir (i, " es primo")
        Cont <- Cont + 1
      Fin Si
    Fin Desde
    Escribir ("Entre 1 y 1000 hay ", Cont, " números primos")
  Fin

(hecho en clase terminado en casa)

'''

primer_numero = 1
limite = 1000
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