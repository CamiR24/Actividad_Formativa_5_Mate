'''
Camila Richter 23183
Marinés García 23391
Ángel Esquit 23221

Actividad Formativa #5
    Criba
'''

import time

# Función para generar primos usando la criba de Eratóstenes
def criba(n):
    prime: list = []
    not_primes = set()

    # Bucle principal para encontrar números primos
    for i in range(2, int(n**0.5) + 1):
        if i in not_primes:
            continue  # Si el número está marcado como no primo, saltar

        # Marcar todos los múltiplos de i como no primos, empezando desde i * i
        for j in range(i * i, n + 1, i):
            not_primes.add(j)

    # Si el número ⁠ n ⁠ no está en ⁠ not_primes ⁠, es primo
    primes = [i for i in range(2, n + 1) if i not in not_primes]

    return primes

print("\n=== CRIBA ===")

# Ingreso del número
a = int(input("Ingrese un número: "))

# Medición de tiempo
start_time = time.time()

prime = criba(a)

end_time = time.time()

# Imprimir la lista de números primos y el tiempo de ejecución
print(f"Los números primos menores o iguales a {a} son: {prime}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")