def camino_tesoro(mapa_str):
    filas = mapa_str.split(";")
    mapa = [fila.split(",") for fila in filas]
    fila = 0
    columna = 0
    delta_fila = 0
    delta_columna = 1

    while True:
        valor = mapa[fila][columna]

        if valor == "T":
            print("¡Has encontrado el tesoro en la fila: " + str(fila) +
                  " y columna: " + str(columna) + "!")
            break
        elif valor == "A":
            delta_fila = -1
            delta_columna = 0
            print("Te moviste hacia arriba")
        elif valor == "B":
            delta_fila = 1
            delta_columna = 0
            print("Te moviste hacia abajo")
        elif valor == "I":
            delta_fila = 0
            delta_columna = -1
            print("Te moviste hacia la izquierda")
        elif valor == "D":
            delta_fila = 0
            delta_columna = 1
            print("Te moviste hacia la derecha")

        fila += delta_fila
        columna += delta_columna

        if columna >= len(mapa[0]):
            fila += 1
            columna = 0
        if fila >= len(mapa):
            print("Error: No se encontró el tesoro.")
            break

