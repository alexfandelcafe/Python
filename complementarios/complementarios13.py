'''
Para una empresa con N empleados, se desarrolla un
algoritmo donde se ingresa como datos el número de orden y
sueldo de cada empleado, debe imprimirse el numero de orden
del empleado con el mayor sueldo asi como su sueldo. Haga
el algoritmo correspondiente.

'''

N = int(input("Ingrese la cantidad de empleados: "))

numero_orden_mayor_sueldo = None
mayor_sueldo = float('-inf')  # inicializar con el valor negativo infinito

for i in range(1, N + 1):
    numero_orden = int(input("Ingrese el número de orden del empleado " + str(i) + ": "))
    sueldo = float(input("Ingrese el sueldo del empleado " + str(i) + ": "))
    
    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        numero_orden_mayor_sueldo = numero_orden

print("El empleado con el mayor sueldo es el número de orden", numero_orden_mayor_sueldo, "con sueldo de", mayor_sueldo)