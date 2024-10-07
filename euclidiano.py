'''
Actividad Formativa #5
    Algoritmo Euclidiano
'''

import time

def mcd(a, b):
    r = a % b  # residuo división
    while r != 0:  # mientras residuo no sea 0...
        r = a % b  # calcula el nuevo residuo
        a = b      # a toma el valor de b
        b = r      # b toma el valor del residuo
    return a


print("\n=== EUCLIDIANO ==")

a = int(input("Ingrese un entero positivo a: ")) #Input usuario
b = int(input("Ingrese otro entero positivo b: ")) #Input usuario

start_time = time.time()

print("El MCD de", a, "y", b, "es:", mcd(a,b))

end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos") #Tiempo de ejecución
