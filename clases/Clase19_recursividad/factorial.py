#Calcular el factorial de un numero sin recursividad
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))

#Calcular el factorial de un numero con recursividad
def factorial_recursividad(n):
    if n == 0:
        return 1
    return n * factorial_recursividad(n-1)

print(factorial_recursividad(100))