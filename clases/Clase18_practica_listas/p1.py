def encontrar_tesoro(mapa_str):
    filas = mapa_str.split(";")
    mapa = [fila.split(",") for fila in filas]
    trampas = 0
    fila_tesoro = 0
    columna_tesoro = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "X":
                trampas += 1
            elif mapa[i][j] == "T":
                return [ i, j, trampas]