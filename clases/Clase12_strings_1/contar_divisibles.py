x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))
contador = 0

while True:
    numero = int(input("Ingresa un número (o -1 para terminar): "))
    if numero == -1:
        break
    if numero % x == 0 or numero % y == 0:
        contador += 1

print("Cantidad de números divisibles entre", x, "o", y,":",contador)
