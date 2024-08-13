def fibonacci(n):
    """
    Calcula el n-ésimo número de la sucesión de Fibonacci.

    Parámetros:
        n (int): El número de la sucesión de Fibonacci que se desea calcular.

    Retorno:
        int: El n-ésimo número de la sucesión de Fibonacci.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Generar la sucesión de Fibonacci hasta el número 10
for i in range(11):
    print(fibonacci(i), end=" ")
print()



