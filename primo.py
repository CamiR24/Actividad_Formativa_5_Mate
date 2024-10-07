'''
Actividad Formativa #5
    ifPrime
'''

import time

# Función para generar primos usando la criba de Eratóstenes
def criba(n):
    not_primes = set()

    # Bucle principal para encontrar números primos
    for i in range(2, int(n**0.5) + 1):
        if i in not_primes:
            continue  # Si el número está marcado como no primo, saltar

        # Marcar todos los múltiplos de i como no primos, empezando desde i * i
        for j in range(i * i, n + 1, i):
            not_primes.add(j)

    # Generar la lista de primos como los números que no están en not_primes
    primes = [i for i in range(2, n + 1) if i not in not_primes]

    return primes

# Función para verificar si un número es primo y encontrar sus divisores primos
def is_prime(n):
    if n < 2:
        return False, []

    # Generar lista de primos hasta raíz de n
    primes = criba(int(n**0.5) + 1)

    # Verificar si n es divisible por algún primo y recolectar todos los divisores
    divisors = [primeNumber for primeNumber in primes if n % primeNumber == 0]

    if len(divisors) > 0:
        return False, divisors  # n no es primo, devolver todos los divisores primos

    return True, []  # n es primo

print("\n=== NÚMEROS PRIMOS ===")
# Ingreso del número
a = int(input("Ingrese un número entero positivo n: "))

# Medición de tiempo
start_time = time.time()
prime, divisors = is_prime(a)  # Verificar si es primo y obtener divisores
end_time = time.time()

# Imprimir si el número es primo o no, y sus divisores si no lo es

if prime:
    print(f"El número {a} es primo.")
else:
    print(f"El número {a} no es primo, pues lo dividen los números primos {divisors}.")

print(f"Tiempo de ejecución: {end_time - start_time} segundos")
