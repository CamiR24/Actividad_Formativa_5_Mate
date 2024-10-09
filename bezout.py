'''
Camila Richter 23183
Marinés García 23391
Ángel Esquit 23221

Actividad Formativa #5
    Bézout
'''

def multiplicador_matrices(A, B):
    # Inicializamos una matriz de resultado 2x2 con ceros
    resultado = [[0, 0],
                 [0, 0]]

    # Multiplicamos las matrices A y B
    for i in range(2):
        for j in range(2):
            resultado[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]
    
    return resultado

def factores(a, b):
    # Inicializamos la lista de factores
    factores = []

    if a > b: # Si a es mayor que b
        r = a % b
        while r != 0:
            r = a % b
            x = int(a / b)
            a = b
            b = r
            factores.append(x)
    elif b > a: # Si b es mayor que a
        r = b % a
        while r != 0:
            r = b % a
            x = int(b / a)
            b = a
            a = r
            factores.append(x)
    elif a == b: # Si a es igual a b
        factores.append(1)
    return factores

print("\n=== BÉZOUT ===")

# Ingreso de los enteros
entero1 = int(input("Ingrese un entero positivo a: "))
entero2 = int(input("Ingrese otro entero positivo b: "))

# Cálculo de los factores
factores = factores(entero1, entero2)

# Inicializamos las matrices y el resultado
matrices = []
resultado = [[1, 0], [0, 1]]

for i in range(len(factores)): # Generamos las matrices con los factores
    matrices.append([[factores[i], 1],
                     [1, 0]])
    
for i in range(len(matrices)): # Multiplicamos las matrices
    a = matrices[i]
    resultado = multiplicador_matrices(resultado, a)

# Imprimimos los resultados
print(f"\nLos coeficientes de Bézout de {entero1} y {entero2} son {resultado[1][1]} y {-resultado[0][1]}, respectivamente.")
print(f"La ecuación diofántica es: ({resultado[1][1]})*{entero1} + ({-resultado[0][1]})*{entero2} = {resultado[1][1]*entero1 + -resultado[0][1]*entero2}\n")