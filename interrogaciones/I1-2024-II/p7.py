# Escribe tu código aquí
from diccionario import valida


def corregir_2(palabra, pos1, pos2):
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    for letra in abecedario:
        palabra_nueva = palabra[:pos1] + letra + palabra[pos1 + 1:]
        for letra2 in abecedario:
            palabra_nueva = palabra_nueva[:pos2] + letra2 + palabra_nueva[pos2 + 1:]
            if valida(palabra_nueva):
                return palabra_nueva

    return palabra
