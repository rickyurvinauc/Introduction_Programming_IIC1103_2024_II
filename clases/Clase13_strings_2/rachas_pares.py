def contar_rachas_pares():
    rachas = 0

    # Inicializamos con tres variables para almacenar los tres últimos números ingresados
    num1 = int(input("Ingresa un número (o -1 para terminar): "))
    num2 = int(input("Ingresa un número (o -1 para terminar): "))
    num3 = int(input("Ingresa un número (o -1 para terminar): "))

    # Verificamos si los tres primeros números forman una racha de pares
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        rachas += 1

    nuevo_num = int(input("Ingresa el siguiente número (o -1 para terminar): "))

    while nuevo_num != -1:
        # Ingresamos el siguiente número
        # if nuevo_num == -1:
        #     break

        # Movemos los números: num1 -> num2, num2 -> num3, num3 -> nuevo_num
        num1 = num2
        num2 = num3
        num3 = nuevo_num

        # Verificamos si los nuevos tres números forman una racha de pares
        if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
            rachas += 1
        nuevo_num = int(input("Ingresa el siguiente número (o -1 para terminar): "))

    # Imprimimos el número total de rachas de pares consecutivos
    print("Número de rachas de pares:", rachas)


# Ejecutar la función
contar_rachas_pares()
